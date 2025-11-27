from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import perform_inference


class PredictionView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user_id = request.data.get('user_id')
        features = request.data.get('features', {})

        if not user_id:
            return Response({'error': 'user_id is required.'}, status=status.HTTP_400_BAD_REQUEST)

        churn_risk, retention_message = perform_inference(user_id, features)
        return Response({
            'user_id': user_id,
            'churn_risk': churn_risk,
            'retention_message': retention_message,
        })
