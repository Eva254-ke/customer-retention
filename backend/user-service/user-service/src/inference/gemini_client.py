import json
import logging
import os
from typing import Any, Dict, Optional

import requests


logger = logging.getLogger(__name__)


_GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not _GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is required")

_GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-2.5-flash")
if not _GEMINI_MODEL_NAME:
    raise ValueError("GEMINI_MODEL_NAME environment variable is required")

_GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{_GEMINI_MODEL_NAME}:generateContent"

_SESSION = requests.Session()


def _build_prompt(user_id: str, risk: float, features: Dict[str, Any]) -> str:
    """Build a concise SMS-style prompt for Gemini based on churn risk and features."""
    base_context = (
        "You are a retention assistant for a consumer app. "
        "Write a short, friendly SMS (<= 160 characters) encouraging the user to come back. "
        "Do not add any labels like 'SMS:' or explanations, only the message body. "
        "If the user has provided a phone number, include it in the message. "
        "The phone number may be in the features dictionary under 'phone_number' key. "
        "If the phone number is not available, do not include it."
    )

    safe_features = {k: v for k, v in features.items() if isinstance(k, str)}

    details = {
        "user_id": user_id,
        "churn_risk": round(float(risk), 3),
        "features": safe_features,
    }

    return f"{base_context}\nUser context: {json.dumps(details, ensure_ascii=False)}"


def generate_retention_message(user_id: str, risk: float, features: Dict[str, Any]) -> str:
    """Call Gemini to generate a personalized retention SMS.

    Returns a short message string or raises ValueError if generation fails
    or the response has no usable text.
    """
    prompt = _build_prompt(user_id=user_id, risk=risk, features=features)

    payload: Dict[str, Any] = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": prompt},
                ],
            }
        ],
        # Keep temperature at 1.0 as recommended for Gemini 3 models and
        # avoid an aggressive max token cap so that the model has room
        # to respond fully.
        "generationConfig": {
            "temperature": 1.0,
        },
    }

    params = {"key": _GEMINI_API_KEY}

    try:
        response = _SESSION.post(_GEMINI_ENDPOINT, json=payload, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as exc:  # noqa: BLE001
        logger.error("Gemini API call failed: %s", exc)
        raise ValueError(f"Gemini API call failed: {exc}") from exc

    candidates = data.get("candidates") or []
    if not candidates:
        logger.error("Gemini API returned no candidates: %s", data)
        raise ValueError("Gemini API returned no candidates")

    first = candidates[0]
    content = first.get("content") or {}
    parts = content.get("parts") or []

    for part in parts:
        text = part.get("text")
        if isinstance(text, str) and text.strip():
            message = text.strip()
            # Keep the SMS reasonably short, but do not hard-fail on length.
            if len(message) > 480:
                message = message[:480]
            return message

    logger.error("Gemini API response had no usable text parts: %s", data)
    raise ValueError("Gemini API response had no usable text parts")
