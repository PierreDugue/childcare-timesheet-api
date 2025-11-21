from rest_framework import serializers
from .models import Family, FamilyLog


class FamilyLogSerializer(serializers.ModelSerializer):
    startHour = serializers.CharField(source='start_hour', allow_blank=True, required=False)
    endHour = serializers.CharField(source='end_hour', allow_blank=True, required=False)
    
    class Meta:
        model = FamilyLog
        fields = ['id', 'family', 'date', 'startHour', 'endHour', 'comment', 'signature']


class FamilySerializer(serializers.ModelSerializer):
    logs = FamilyLogSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Family
        fields = ['familyId', 'user', 'name', 'logs']
