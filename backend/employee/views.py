"""
Views for the employee API.
"""
from employee import serializers
from rest_framework.response import Response
from core.models import Employee
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class EmployeeViewSet(ViewSet):
    """View to Retrieve, Manage & Destroy employee."""
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.EmployeeSerializer

    def list(self,request):
        """Get list of employees."""
        try:
            employee_objs = Employee.objects.all()
            serializer = serializers.EmployeeSerializer(employee_objs, many=True)

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
        """Retrieve employee details."""
        try:
            id = pk
            if id is not None:
                employee_obj = serializers.Employee.objects.get(id=id)
                serializer = serializers.EmployeeSerializer(employee_obj)
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
        """Get request data & create employee."""
        try:
            serializer = serializers.EmployeeSerializer(data = request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'errors':serializer.errors,
                    'message':'Invalid data.'
                })

            serializer.save()
            return Response({
                'status':status.HTTP_201_CREATED,
                'data':serializer.data,
                'message':'Employee added successfully.'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })


    def update(self,request, pk):
        """Get request data & update employee."""
        try:
            id = pk
            employee_obj = Employee.objects.get(pk=id)
            serializer = serializers.EmployeeSerializer(employee_obj, data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'errors':serializer.errors,
                    'message':'Invalid data.'
                })

            serializer.save()
            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data,
                'message':'Employee updated successfully.'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

    def partial_update(self,request, pk):
        """Get request data & patch employee."""
        try:
            id = pk
            employee_obj = Employee.objects.get(pk=id)
            serializer = serializers.EmployeeSerializer(employee_obj, data=request.data, partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'errors':serializer.errors,
                    'message':'Invalid data.'
                })

            serializer.save()
            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data,
                'message':'Employee patched successfully.'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

    def destroy(self,request, pk):
        """Remove employee."""
        try:
            id = pk
            employee_obj = Employee.objects.get(pk=id)

            employee_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'message':'Employee deleted successfully.'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })
