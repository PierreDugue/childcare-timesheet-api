from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FamilyViewSet, FamilyLogViewSet

router = DefaultRouter()
router.register(r'families', FamilyViewSet)
router.register(r'logs', FamilyLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
