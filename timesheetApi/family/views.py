from rest_framework import viewsets, permissions
from .models import Family, FamilyLog
from .serializers import FamilySerializer, FamilyLogSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView

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

class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]  # anyone can register

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not username or not email or not password:
            return Response({"detail": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"detail": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({"detail": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )

        return Response({"detail": "User created successfully."}, status=status.HTTP_201_CREATED)