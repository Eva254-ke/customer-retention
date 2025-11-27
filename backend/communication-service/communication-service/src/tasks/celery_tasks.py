from celery import Celery
from services.africas_talking import send_sms
from services.messaging import create_message

app = Celery('communication_service', broker='redis://localhost:6379/0')

@app.task
def send_personalized_sms(phone_number, message):
    """Send a personalized SMS to the user."""
    sms_message = create_message(message)
    send_sms(phone_number, sms_message)

@app.task
def retry_failed_sms(sms_id):
    """Retry sending a failed SMS based on its ID."""
    # Logic to retrieve the SMS details and resend
    pass

@app.task
def schedule_sms(phone_number, message, schedule_time):
    """Schedule an SMS to be sent at a specific time."""
    # Logic to schedule the SMS
    pass