from rest_framework import serializers
from .models import Family, FamilyLog


class FamilyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyLog
        fields = "__all__"


class FamilySerializer(serializers.ModelSerializer):
    logs = FamilyLogSerializer(many=True, read_only=True)

    class Meta:
        model = Family
        fields = "__all__"
