import csv
import io

from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserPreferencesSerializer, UserSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class BulkUploadUsersView(APIView):
    """Bulk upload users from CSV file."""
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        if not file.name.endswith('.csv'):
            return Response({'error': 'File must be a CSV'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            decoded = file.read().decode('utf-8')
            reader = csv.DictReader(io.StringIO(decoded))
        except Exception as e:
            return Response({'error': f'Failed to parse CSV: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        created = []
        updated = []
        errors = []

        for row_num, row in enumerate(reader, start=2):  # Start at 2 (header is row 1)
            try:
                email = row.get('email', '').strip()
                if not email:
                    errors.append({'row': row_num, 'error': 'Email is required'})
                    continue

                first_name = row.get('first_name', '').strip()
                last_name = row.get('last_name', '').strip()
                phone_number = row.get('phone_number', '').strip()

                # Build preferences from extra fields
                preferences = {}
                for key in ['engagement_score', 'last_active_days', 'rides_last_30_days', 'city', 'segment']:
                    if key in row and row[key].strip():
                        val = row[key].strip()
                        # Try to convert numeric values
                        if key in ['engagement_score']:
                            try:
                                preferences[key] = float(val)
                            except ValueError:
                                preferences[key] = val
                        elif key in ['last_active_days', 'rides_last_30_days']:
                            try:
                                preferences[key] = int(val)
                            except ValueError:
                                preferences[key] = val
                        else:
                            preferences[key] = val

                # Generate username from email
                username = email.split('@')[0]
                base_username = username
                counter = 1
                while User.objects.filter(username=username).exclude(email=email).exists():
                    username = f"{base_username}{counter}"
                    counter += 1

                user, was_created = User.objects.update_or_create(
                    email=email,
                    defaults={
                        'username': username,
                        'first_name': first_name,
                        'last_name': last_name,
                        'phone_number': phone_number,
                        'preferences': preferences,
                    }
                )

                if was_created:
                    created.append({'id': user.id, 'email': email, 'name': f"{first_name} {last_name}"})
                else:
                    updated.append({'id': user.id, 'email': email, 'name': f"{first_name} {last_name}"})

            except Exception as e:
                errors.append({'row': row_num, 'error': str(e)})

        return Response({
            'created': len(created),
            'updated': len(updated),
            'errors': len(errors),
            'details': {
                'created': created,
                'updated': updated,
                'errors': errors[:10],  # Limit error details
            }
        }, status=status.HTTP_200_OK if not errors else status.HTTP_207_MULTI_STATUS)


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
