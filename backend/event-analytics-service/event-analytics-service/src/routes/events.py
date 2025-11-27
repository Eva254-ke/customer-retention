from flask import Blueprint, request, jsonify
from services.analytics import process_event

events_bp = Blueprint('events', __name__)

@events_bp.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    try:
        event_id = process_event(data)
        return jsonify({'event_id': event_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500