from rest_framework import viewsets
from .models import Family, FamilyLog
from .serializers import FamilySerializer, FamilyLogSerializer


class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    lookup_field = 'familyId'

class FamilyLogViewSet(viewsets.ModelViewSet):
    queryset = FamilyLog.objects.all()
    serializer_class = FamilyLogSerializer
