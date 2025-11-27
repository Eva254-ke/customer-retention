from django.urls import path

from .views import CommunicationsStatusView, SendSMSView, TaskStatusView

urlpatterns = [
    path('send-sms/', SendSMSView.as_view(), name='send-sms'),
    path('status/', CommunicationsStatusView.as_view(), name='communications-status'),
    path('tasks/<str:task_id>/', TaskStatusView.as_view(), name='sms-task-status'),
]
