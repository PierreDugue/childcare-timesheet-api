from rest_framework import viewsets, permissions
from .models import Family, FamilyLog
from .serializers import FamilySerializer, FamilyLogSerializer
from rest_framework.response import Response
from rest_framework import status


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

    def create(self, request, *args, **kwargs):
        family_id = request.data.get('family')
        date = request.data.get('date')

        # Try to find an existing log with the same family and date
        existing_log = FamilyLog.objects.filter(family_id=family_id, date=date).first()

        if existing_log:
            # Update existing log
            serializer = self.get_serializer(existing_log, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Create a new log
            return super().create(request, *args, **kwargs)
