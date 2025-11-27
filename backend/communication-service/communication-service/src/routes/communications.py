from flask import Blueprint, request, jsonify
from services.africas_talking import send_sms
from tasks.sms_queue import enqueue_sms_task, get_sms_task

communications_bp = Blueprint('communications', __name__)

@communications_bp.route('/send-sms', methods=['POST'])
def send_sms_route():
    data = request.json
    phone_number = data.get('phone_number')
    message = data.get('message')

    if not phone_number or not message:
        return jsonify({'error': 'Phone number and message are required.'}), 400

    if data.get('async', False):
        task = enqueue_sms_task(phone_number, message)
        return jsonify({'status': 'queued', 'task': task}), 202

    response = send_sms(phone_number, message)
    return jsonify({'status': 'success', 'response': response}), 200

@communications_bp.route('/status', methods=['GET'])
def status_route():
    return jsonify({'status': 'Communication service is running.'}), 200


@communications_bp.route('/tasks/<task_id>', methods=['GET'])
def task_status_route(task_id):
    task = get_sms_task(task_id)
    if not task:
        return jsonify({'error': 'Task not found.'}), 404
    return jsonify(task), 200
