"""
Serializers for the designation API View.
"""
from rest_framework import serializers

from core.models import Designation

class DesignationSerializer(serializers.ModelSerializer):
    """DesignationSerializer to get designation details."""
    name = serializers.CharField(max_length=255,allow_blank=True)

    class Meta:
        model = Designation
        # fields = ['id', 'name']
        # exclude = ['id']
        fields = '__all__'
        read_only_fields = ['id']

    def validate(self, data):

        if len(data['name']) == 0:
            raise serializers.ValidationError({'error':'name required'})

        return data
