from rest_framework import viewsets, permissions
from .models import Family, FamilyLog
from .serializers import FamilySerializer, FamilyLogSerializer


class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Family.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FamilyLogViewSet(viewsets.ModelViewSet):
    queryset = FamilyLog.objects.all()
    serializer_class = FamilyLogSerializer
