from django.db import models

class Event(models.Model):
    event_type = models.CharField(max_length=255)
    user_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField()

    def __str__(self):
        return f"{self.event_type} for user {self.user_id} at {self.timestamp}"