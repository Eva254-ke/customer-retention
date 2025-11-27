from django.urls import path
from .views import UserListView, UserDetailView, UserPreferencesView, BulkUploadUsersView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('bulk-upload/', BulkUploadUsersView.as_view(), name='user-bulk-upload'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/preferences/', UserPreferencesView.as_view(), name='user-preferences'),
]
