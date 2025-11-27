from flask import Blueprint, request, jsonify
from services.groq_client import GroqClient
from models.churn import ChurnModel

inference_bp = Blueprint('inference', __name__)

@groq_client = GroqClient()

@inference_bp.route('/predict', methods=['POST'])
def predict_churn():
    data = request.json
    user_id = data.get('user_id')
    user_data = data.get('user_data')

    if not user_id or not user_data:
        return jsonify({'error': 'user_id and user_data are required'}), 400

    churn_risk = churn_model.predict(user_data)

    if churn_risk > 0.5:  # Example threshold
        message = groq_client.generate_message(user_id, churn_risk)
        return jsonify({'churn_risk': churn_risk, 'message': message}), 200

    return jsonify({'churn_risk': churn_risk, 'message': 'No action needed'}), 200