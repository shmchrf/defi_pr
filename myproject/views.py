# systems/views.py

from rest_framework import viewsets
from .models import HumanSystem, OceanSystem, Comparison
from .serializers import HumanSystemSerializer, OceanSystemSerializer, ComparisonSerializer

class HumanSystemViewSet(viewsets.ModelViewSet):
    queryset = HumanSystem.objects.all()
    serializer_class = HumanSystemSerializer

class OceanSystemViewSet(viewsets.ModelViewSet):
    queryset = OceanSystem.objects.all()
    serializer_class = OceanSystemSerializer

class ComparisonViewSet(viewsets.ModelViewSet):
    queryset = Comparison.objects.all()
    serializer_class = ComparisonSerializer
