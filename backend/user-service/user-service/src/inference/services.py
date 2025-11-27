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

    # Always generate a personalized message via Gemini; errors from
    # generate_retention_message will propagate to the caller.
    message: Any = generate_retention_message(user_id=user_id, risk=risk, features=features)  # type: ignore[arg-type]
    source = RetentionMessage.Source.GEMINI
    RetentionMessage.objects.create(
        user_id=user_id,
        risk=float(risk),
        features=dict(features),
        message=str(message),
        source=source,
    )

    return round(risk, 3), str(message)


