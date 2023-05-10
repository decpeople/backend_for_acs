from rest_framework import serializers
from django.db import models
from .models import AirCompany, Rotating, Command, Food, Image, Flight

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']

class FoodSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Food
        fields = ['id', 'food', 'images']

class CommandSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True)

    class Meta:
        model = Command
        fields = ['id', 'command', 'foods']

class RotatingSerializer(serializers.ModelSerializer):
    commands = CommandSerializer(many=True)

    class Meta:
        model = Rotating
        fields = ['id', 'rotation', 'commands']

class AirCompanySerializer(serializers.ModelSerializer):
    rotatings = RotatingSerializer(many=True)

    class Meta:
        model = AirCompany
        fields = ['id', 'name', 'rotatings']

class FlightSerializer(serializers.ModelSerializer):
    air_company = AirCompanySerializer(many=True)

    class Meta:
        model = Flight
        fields = ['id', 'air_company']
