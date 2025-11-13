from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FamilyViewSet, FamilyLogViewSet, RegisterAPIView

router = DefaultRouter()
router.register(r'families', FamilyViewSet)
router.register(r'logs', FamilyLogViewSet)

urlpatterns = [    
    path("register/", RegisterAPIView.as_view(), name="register"),
    path('', include(router.urls)),
]
