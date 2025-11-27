from flask import Blueprint, request, jsonify
from services.inference import perform_inference

predictions_bp = Blueprint('predictions', __name__)

@predictions_bp.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if not data or 'user_id' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    user_id = data['user_id']
    churn_risk, retention_message = perform_inference(user_id)

    return jsonify({
        'user_id': user_id,
        'churn_risk': churn_risk,
        'retention_message': retention_message
    })