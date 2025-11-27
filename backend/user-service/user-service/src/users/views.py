from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import User
from .serializers import UserPreferencesSerializer, UserSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserPreferencesView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserPreferencesSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def patch(self, request, pk):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
