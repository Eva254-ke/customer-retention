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
