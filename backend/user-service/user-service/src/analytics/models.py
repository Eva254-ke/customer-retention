from django.db import models


class Event(models.Model):
    event_type = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.event_type} for user {self.user_id}"
