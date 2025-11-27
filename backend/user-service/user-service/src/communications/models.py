from django.db import models


class SMSMessage(models.Model):
    class Direction(models.TextChoices):
        OUTGOING = 'outgoing', 'Outgoing'
        INCOMING = 'incoming', 'Incoming'

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        QUEUED = 'queued', 'Queued'
        PROCESSING = 'processing', 'Processing'
        SENT = 'sent', 'Sent'
        FAILED = 'failed', 'Failed'

    direction = models.CharField(max_length=10, choices=Direction.choices, default=Direction.OUTGOING)
    phone_number = models.CharField(max_length=32)
    message = models.TextField()
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.PENDING)
    task_id = models.CharField(max_length=64, blank=True, null=True)
    provider_response = models.JSONField(default=dict, blank=True)
    error = models.TextField(blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.direction} SMS to {self.phone_number} ({self.status})"
