from typing import Any, Dict
import requests

class GroqClient:
    def __init__(self, api_key: str, base_url: str = "https://api.groq.com"):
        self.api_key = api_key
        self.base_url = base_url

    def predict_churn(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/predict"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(endpoint, json=user_data, headers=headers)
        response.raise_for_status()
        return response.json()

    def generate_retention_message(self, user_id: str, churn_risk: float) -> str:
        endpoint = f"{self.base_url}/generate-message"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "user_id": user_id,
            "churn_risk": churn_risk
        }
        response = requests.post(endpoint, json=payload, headers=headers)
        response.raise_for_status()
        return response.json().get("message", "")