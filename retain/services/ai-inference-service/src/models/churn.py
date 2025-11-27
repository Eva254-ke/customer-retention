from django.db import models

class ChurnPrediction(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    churn_risk_score = models.FloatField()
    last_interaction_date = models.DateTimeField()
    predicted_churn_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ChurnPrediction(user_id={self.user_id}, risk_score={self.churn_risk_score})"