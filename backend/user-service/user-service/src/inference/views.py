from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from communications.models import SMSMessage
from communications.services import send_sms
from .services import perform_inference


class PredictionView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user_id = request.data.get('user_id')
        features = request.data.get('features', {})

        if not user_id:
            return Response({'error': 'user_id is required.'}, status=status.HTTP_400_BAD_REQUEST)

        churn_risk, retention_message = perform_inference(user_id, features)

        sms_info = None
        phone_number = features.get('phone_number')
        if phone_number:
            sms_record = SMSMessage.objects.create(
                direction=SMSMessage.Direction.OUTGOING,
                phone_number=phone_number,
                message=retention_message,
                status=SMSMessage.Status.PENDING,
            )
            try:
                provider_response = send_sms(phone_number, retention_message)
                sms_record.status = SMSMessage.Status.SENT
                sms_record.provider_response = provider_response
                sms_record.save(update_fields=['status', 'provider_response', 'updated_at'])
                sms_info = {
                    'message_id': sms_record.id,
                    'status': sms_record.status,
                    'provider_response': provider_response,
                }
            except Exception as exc:  # noqa: BLE001
                sms_record.status = SMSMessage.Status.FAILED
                sms_record.error = str(exc)
                sms_record.save(update_fields=['status', 'error', 'updated_at'])
                sms_info = {
                    'message_id': sms_record.id,
                    'status': sms_record.status,
                    'error': str(exc),
                }

        return Response({
            'user_id': user_id,
            'churn_risk': churn_risk,
            'retention_message': retention_message,
            'sms': sms_info,
        })
