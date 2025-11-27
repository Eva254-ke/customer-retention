from flask import Blueprint, request, jsonify
from services.africas_talking import send_sms
from tasks.celery_tasks import send_sms_task

communications_bp = Blueprint('communications', __name__)

@communications_bp.route('/send-sms', methods=['POST'])
def send_sms_route():
    data = request.json
    phone_number = data.get('phone_number')
    message = data.get('message')

    if not phone_number or not message:
        return jsonify({'error': 'Phone number and message are required.'}), 400

    # Send SMS synchronously
    response = send_sms(phone_number, message)

    # Optionally, you can send SMS asynchronously using Celery
    # send_sms_task.delay(phone_number, message)

    return jsonify({'status': 'success', 'response': response}), 200

@communications_bp.route('/status', methods=['GET'])
def status_route():
    return jsonify({'status': 'Communication service is running.'}), 200