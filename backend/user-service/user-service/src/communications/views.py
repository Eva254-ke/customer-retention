from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SMSMessage
from .services import send_sms
from .tasks.sms_queue import enqueue_sms_task, get_sms_task


class SendSMSView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone_number = request.data.get('phone_number')
        message = request.data.get('message')

        if not phone_number or not message:
            return Response({'error': 'phone_number and message are required.'}, status=status.HTTP_400_BAD_REQUEST)

        sms_record = SMSMessage.objects.create(
            direction=SMSMessage.Direction.OUTGOING,
            phone_number=phone_number,
            message=message,
            status=SMSMessage.Status.PENDING,
        )

        if request.data.get('async', False):
            sms_record.status = SMSMessage.Status.QUEUED
            sms_record.save(update_fields=['status', 'updated_at'])
            task = enqueue_sms_task(phone_number, message, sms_record.id)
            sms_record.task_id = task['id']
            sms_record.save(update_fields=['task_id', 'updated_at'])
            return Response({'status': 'queued', 'task': task, 'message_id': sms_record.id}, status=status.HTTP_202_ACCEPTED)

        try:
            response = send_sms(phone_number, message)
            sms_record.status = SMSMessage.Status.SENT
            sms_record.provider_response = response
            sms_record.save(update_fields=['status', 'provider_response', 'updated_at'])
        except ValueError as exc:
            sms_record.status = SMSMessage.Status.FAILED
            sms_record.error = str(exc)
            sms_record.save(update_fields=['status', 'error', 'updated_at'])
            return Response({'error': str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            sms_record.status = SMSMessage.Status.FAILED
            sms_record.error = str(exc)
            sms_record.save(update_fields=['status', 'error', 'updated_at'])
            return Response({'error': 'Failed to send SMS', 'details': str(exc)}, status=status.HTTP_502_BAD_GATEWAY)

        return Response({'status': 'success', 'response': response, 'message_id': sms_record.id}, status=status.HTTP_200_OK)


class CommunicationsStatusView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'status': 'Communication module is running.'})


class TaskStatusView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, task_id: str):
        task = get_sms_task(task_id)
        if not task:
            return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(task)
