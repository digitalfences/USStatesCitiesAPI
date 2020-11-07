  
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import LocationSerializer, StateSerializer
from .models import Location, State
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class StateList(generics.ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class LocationListByState(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = ( DjangoFilterBackend, )
    filterset_fields = ("state__code",) 
    
class LocationDetail(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
