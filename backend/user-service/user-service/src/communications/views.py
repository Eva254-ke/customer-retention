from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import send_sms
from .tasks.sms_queue import enqueue_sms_task, get_sms_task


class SendSMSView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone_number = request.data.get('phone_number')
        message = request.data.get('message')

        if not phone_number or not message:
            return Response({'error': 'phone_number and message are required.'}, status=status.HTTP_400_BAD_REQUEST)

        if request.data.get('async', False):
            task = enqueue_sms_task(phone_number, message)
            return Response({'status': 'queued', 'task': task}, status=status.HTTP_202_ACCEPTED)

        try:
            response = send_sms(phone_number, message)
        except ValueError as exc:
            return Response({'error': str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            return Response({'error': 'Failed to send SMS', 'details': str(exc)}, status=status.HTTP_502_BAD_GATEWAY)

        return Response({'status': 'success', 'response': response}, status=status.HTTP_200_OK)


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
