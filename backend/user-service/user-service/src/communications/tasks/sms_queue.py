from typing import Any, Dict, Optional

from communications.models import SMSMessage
from communications.services import send_sms
from .in_memory_db import InMemoryDB, SimpleTaskQueue

_db = InMemoryDB()
_queue = SimpleTaskQueue(_db, queue_name="sms_queue", collection="sms_tasks")


def _process_sms_task(payload: Dict[str, Any]) -> None:
    phone_number = payload["phone_number"]
    message = payload["message"]
    sms_message_id = payload.get("sms_message_id")

    sms_record = None
    if sms_message_id:
        sms_record = SMSMessage.objects.filter(id=sms_message_id).first()
        if sms_record:
            sms_record.status = SMSMessage.Status.PROCESSING
            sms_record.save(update_fields=['status', 'updated_at'])

    try:
        response = send_sms(phone_number, message)
        if sms_record:
            sms_record.status = SMSMessage.Status.SENT
            sms_record.provider_response = response
            sms_record.save(update_fields=['status', 'provider_response', 'updated_at'])
    except Exception as exc:
        if sms_record:
            sms_record.status = SMSMessage.Status.FAILED
            sms_record.error = str(exc)
            sms_record.save(update_fields=['status', 'error', 'updated_at'])
        raise


_queue.register_handler(_process_sms_task)
_queue.start()


def enqueue_sms_task(phone_number: str, message: str, sms_message_id: Optional[int] = None) -> Dict[str, Any]:
    return _queue.enqueue(
        {
            "phone_number": phone_number,
            "message": message,
            "sms_message_id": sms_message_id,
        }
    )


def get_sms_task(task_id: str) -> Optional[Dict[str, Any]]:
    sms_record = SMSMessage.objects.filter(task_id=task_id).first()
    if sms_record:
        return {
            'message_id': sms_record.id,
            'status': sms_record.status,
            'phone_number': sms_record.phone_number,
            'error': sms_record.error,
            'provider_response': sms_record.provider_response,
            'updated_at': sms_record.updated_at.isoformat(),
        }
    return _queue.get_task(task_id)
