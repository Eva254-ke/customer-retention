from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.exceptions import AuthenticationFailed

class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            raise AuthenticationFailed('No authentication token provided.')

        try:
            user = self.get_user_from_token(token)
            request.user = user
        except Exception as e:
            raise AuthenticationFailed(f'Authentication failed: {str(e)}')

    def get_user_from_token(self, token):
        # Logic to decode the token and retrieve the user
        # This is a placeholder for actual token decoding logic
        user_id = self.decode_token(token)
        user = User.objects.get(id=user_id)
        return user

    def decode_token(self, token):
        # Placeholder for token decoding logic
        # In a real implementation, this would decode the JWT or similar token
        return int(token)  # Example: assuming token is user ID for simplicity