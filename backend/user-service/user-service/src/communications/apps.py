from django.apps import AppConfig


class CommunicationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'communications'

    def ready(self):
        # Import queue to ensure the worker thread is started once per process
        from .tasks import sms_queue  # noqa: F401
