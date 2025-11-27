from flask import Blueprint, request, jsonify
import requests

gateway_bp = Blueprint('gateway', __name__)

# Define the service URLs
USER_SERVICE_URL = 'http://user-service:8000'
EVENT_ANALYTICS_SERVICE_URL = 'http://event-analytics-service:8001'
AI_INFERENCE_SERVICE_URL = 'http://ai-inference-service:8002'
COMMUNICATION_SERVICE_URL = 'http://communication-service:8003'

@gateway_bp.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        response = requests.get(f'{USER_SERVICE_URL}/users')
        return jsonify(response.json()), response.status_code
    elif request.method == 'POST':
        response = requests.post(f'{USER_SERVICE_URL}/users', json=request.json)
        return jsonify(response.json()), response.status_code

@gateway_bp.route('/events', methods=['GET', 'POST'])
def events():
    if request.method == 'GET':
        response = requests.get(f'{EVENT_ANALYTICS_SERVICE_URL}/events')
        return jsonify(response.json()), response.status_code
    elif request.method == 'POST':
        response = requests.post(f'{EVENT_ANALYTICS_SERVICE_URL}/events', json=request.json)
        return jsonify(response.json()), response.status_code

@gateway_bp.route('/predictions', methods=['POST'])
def predictions():
    response = requests.post(f'{AI_INFERENCE_SERVICE_URL}/predictions', json=request.json)
    return jsonify(response.json()), response.status_code

@gateway_bp.route('/communications', methods=['POST'])
def communications():
    response = requests.post(f'{COMMUNICATION_SERVICE_URL}/communications', json=request.json)
    return jsonify(response.json()), response.status_code