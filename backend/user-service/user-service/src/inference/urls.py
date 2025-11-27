from django.urls import path

from .views import PredictionView, dashboard

urlpatterns = [
    path('predict/', PredictionView.as_view(), name='predict'),
    path('dashboard/', dashboard, name='inference-dashboard'),
]
