import os
from typing import Optional, Tuple

from africastalking import Africastalking

class AfricaTalkingService:
    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key
        self.africastalking = Africastalking(self.username, self.api_key)

    def send_sms(self, to, message):
        response = self.africastalking.SMS.send(to, message)
        return response

    def send_bulk_sms(self, recipients, message):
        response = self.africastalking.SMS.send(recipients, message)
        return response

    def check_balance(self):
        response = self.africastalking.Account.fetch()
        return response['balance'] if 'balance' in response else None

    def send_voice_call(self, to, message):
        response = self.africastalking.Voice.call(to, message)
        return response

    def send_ussd(self, to, message):
        response = self.africastalking.USSD.send(to, message)
        return response


def _resolve_credentials(username: Optional[str] = None, api_key: Optional[str] = None) -> Tuple[str, str]:
    resolved_username = username or os.getenv('AFRICASTALKING_USERNAME', 'sandbox')
    resolved_api_key = api_key or os.getenv('AFRICASTALKING_API_KEY', 'dummy')
    return resolved_username, resolved_api_key


def send_sms(to: str, message: str, username: Optional[str] = None, api_key: Optional[str] = None):
    resolved_username, resolved_api_key = _resolve_credentials(username, api_key)
    service = AfricaTalkingService(resolved_username, resolved_api_key)
    return service.send_sms(to, message)
