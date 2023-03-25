"""
Views for the designation API.
"""
from designation import serializers
from rest_framework.response import Response
from core.models import Designation
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class DesignationViewSet(ViewSet):
    """View to Retrieve, Manage & Destroy designation."""
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.DesignationSerializer

    def list(self,request):
        """Get list of designations."""
        try:
            designation_objs = Designation.objects.all()
            serializer = serializers.DesignationSerializer(designation_objs, many=True)

            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })


    def retrieve(self, request, pk=None):
        """Retrieve designation details."""
        try:
            id = pk
            if id is not None:
                designation_obj = serializers.Designation.objects.get(id=id)
                serializer = serializers.DesignationSerializer(designation_obj)
                return Response({
                    'status':status.HTTP_200_OK,
                    'data':serializer.data
                })
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })


    def create(self, request):
        """Get request data & create designation."""
        try:
            serializer = serializers.DesignationSerializer(data = request.data)

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
                'data':serializer.data,
                'message':'Designation added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })


    def update(self,request, pk):
        """Get request data & update designation."""
        try:
            id = pk
            designation_obj = Designation.objects.get(pk=id)
            serializer = serializers.DesignationSerializer(designation_obj, data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'errors':serializer.errors,
                    'message':'Invalid data'
                })

            serializer.save()
            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data,
                'message':'Designation updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

    def partial_update(self,request, pk):
        """Get request data & patch designation."""
        try:
            id = pk
            designation_obj = Designation.objects.get(pk=id)
            serializer = serializers.DesignationSerializer(designation_obj, data=request.data, partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'errors':serializer.errors,
                    'message':'Invalid data'
                })

            serializer.save()
            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data,
                'message':'Designation patched successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

    def destroy(self,request, pk):
        """Remove designation."""
        try:
            id = pk
            designation_obj = Designation.objects.get(pk=id)

            designation_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'message':'Designation deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })
