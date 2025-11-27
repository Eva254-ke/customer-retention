from django.urls import path
from .views import UserListView, UserDetailView, UserPreferencesView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/preferences/', UserPreferencesView.as_view(), name='user-preferences'),
]