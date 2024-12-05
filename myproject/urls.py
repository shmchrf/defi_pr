# systems/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HumanSystemViewSet, OceanSystemViewSet, ComparisonViewSet

router = DefaultRouter()
router.register(r'humans', HumanSystemViewSet)
router.register(r'oceans', OceanSystemViewSet)
router.register(r'comparisons', ComparisonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
