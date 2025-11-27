from django.urls import path
from .views import UserListView, UserDetailView, UserPreferencesView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/preferences/', UserPreferencesView.as_view(), name='user-preferences'),
]
