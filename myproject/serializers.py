# systems/serializers.py

from rest_framework import serializers
from .models import HumanSystem, OceanSystem, Comparison

class HumanSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanSystem
        fields = ['id', 'name', 'description']

class OceanSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OceanSystem
        fields = ['id', 'name', 'description']

class ComparisonSerializer(serializers.ModelSerializer):
    human_system = HumanSystemSerializer()
    ocean_system = OceanSystemSerializer()

    class Meta:
        model = Comparison
        fields = ['id', 'human_system', 'ocean_system', 'similarities', 'consequences_of_dysfunction']
