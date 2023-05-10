from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import FlightSerializer, AirCompanySerializer, RotatingSerializer, CommandSerializer, FoodSerializer, ImageSerializer
from .models import Flight, AirCompany, Rotating, Command, Food, Image
   
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    
class AirCompanyViewSet(viewsets.ModelViewSet):
    queryset = AirCompany.objects.all()
    serializer_class = AirCompanySerializer


class RotatingViewSet(viewsets.ModelViewSet):
    queryset = Rotating.objects.all()
    serializer_class = RotatingSerializer


class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
   


