"""
Views for the user API.
"""
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
# from django.contrib.auth.models import User
from rest_framework import generics,status
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema

@extend_schema(auth=[])
class RegisterUserAPIView(APIView):
    """Create User for authentication."""
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request):
        """Get request data & save."""
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'errors':serializer.errors,
                'message':'Invalid data'
            })

        serializer.save()
        return Response({
            'status':status.HTTP_201_CREATED,
            # 'data':serializer.data,
            'message':'User added successfully'
        })


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user

    def get(self, *args):
        """Get authenticated user details."""
        queryset = self.get_object()
        serializer = UserSerializer(queryset)
        return Response({
            'status':status.HTTP_200_OK,
            'data': serializer.data
        })

    def patch(self, request):
        """Get request data & update user partially"""

        queryset = self.get_object()
        serializer = UserSerializer(queryset, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({
                        'status':status.HTTP_400_BAD_REQUEST,
                        'errors':serializer.errors,
                        'message':'Invalid data'
                    })

        serializer.save()
        return Response({
                    'status':status.HTTP_200_OK,
                    'data':serializer.data,
                    'message':'User partially updated successfully.'
                })

    def put(self, request):
        """Get request data & update user"""

        queryset = self.get_object()
        serializer = UserSerializer(queryset, data=request.data)
        if not serializer.is_valid():
            return Response({
                        'status':status.HTTP_400_BAD_REQUEST,
                        'errors':serializer.errors,
                        'message':'Invalid data.'
                    })

        serializer.save()
        return Response({
                    'status':status.HTTP_200_OK,
                    'data':serializer.data,
                    'message':'User updated successfully.'
                })
