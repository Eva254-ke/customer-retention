from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/communications/', include('communications.urls')),
    path('api/inference/', include('inference.urls')),
    path('api/analytics/', include('analytics.urls')),
]
