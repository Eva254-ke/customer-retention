from typing import Any, Dict, Optional

from services.africas_talking import send_sms
from tasks.in_memory_db import InMemoryDB, SimpleTaskQueue


_db = InMemoryDB()
_queue = SimpleTaskQueue(_db, queue_name="sms_queue", collection="sms_tasks")


def _process_sms_task(payload: Dict[str, Any]) -> None:
    phone_number = payload["phone_number"]
    message = payload["message"]
    send_sms(phone_number, message)


_queue.register_handler(_process_sms_task)
_queue.start()


def enqueue_sms_task(phone_number: str, message: str) -> Dict[str, Any]:
    """Queue an SMS for asynchronous delivery."""
    return _queue.enqueue({"phone_number": phone_number, "message": message})


def get_sms_task(task_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve the latest status for a queued SMS task."""
    return _queue.get_task(task_id)
