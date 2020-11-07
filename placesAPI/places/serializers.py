from rest_framework import serializers
from .models import Location, State, Country

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'          
