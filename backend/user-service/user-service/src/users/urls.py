from django.urls import path
from .views import UserListView, UserDetailView, UserPreferencesView, BulkUploadUsersView, download_sample_csv

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('bulk-upload/', BulkUploadUsersView.as_view(), name='user-bulk-upload'),
    path('sample-csv/', download_sample_csv, name='sample-csv'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/preferences/', UserPreferencesView.as_view(), name='user-preferences'),
]
