from __future__ import annotations

import math
from typing import Any, Dict, Tuple

from analytics.models import RetentionMessage
from .gemini_client import generate_retention_message


def perform_inference(user_id: str, features: Dict[str, float] | None = None) -> Tuple[float, str]:
    """Return a deterministic risk score and simple retention message."""
    features = features or {}
    engagement_score = features.get('engagement_score', 0.5)
    last_active_days = features.get('last_active_days', 7)

    risk = min(0.95, max(0.05, 0.6 - engagement_score * 0.4 + math.log1p(last_active_days) * 0.05))

    # First, try to generate a personalized message via Gemini.
    gemini_message = generate_retention_message(user_id=user_id, risk=risk, features=features)  # type: ignore[arg-type]

    if gemini_message:
        message: Any = gemini_message
        source = RetentionMessage.Source.GEMINI
    elif risk > 0.6:
        message = f"Hi {user_id}, we've missed you! Enjoy an exclusive offer when you return today."
        source = RetentionMessage.Source.RULE_BASED
    elif risk > 0.3:
        message = f"Hey {user_id}, here are tailored tips to keep you engaged with our platform."
        source = RetentionMessage.Source.RULE_BASED
    else:
        message = f"Thanks for staying active, {user_id}! Let us know how we can improve."
        source = RetentionMessage.Source.RULE_BASED

    RetentionMessage.objects.create(
        user_id=user_id,
        risk=float(risk),
        features=dict(features),
        message=str(message),
        source=source,
    )

    return round(risk, 3), str(message)


