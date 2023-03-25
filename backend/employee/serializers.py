"""
Serializers for the user API View.
"""
from rest_framework import serializers

from core.models import Employee
from designation.serializers import DesignationSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer for employee"""
    designation_id = serializers.IntegerField(write_only=True)
    designation = DesignationSerializer(read_only=True)
    # designation = serializers.SlugRelatedField(queryset=Employee.objects.all(), slug_field='designation', write_only=True)

    class Meta:
        model = Employee
        fields = ['id','name','designation','designation_id']
        # read_only_fields = ['id']
