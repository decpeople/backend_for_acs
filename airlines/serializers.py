from rest_framework import serializers
from django.db import models
from .models import AirCompany, Rotating, Command, Food, Image, Flight, HotFood

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'images']

class HotFoodSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model =HotFood
        fields = ['id', 'hotfood', 'images']

class FoodSerializer(serializers.ModelSerializer):
    hotfoods = HotFoodSerializer(many=True)

    class Meta:
        model = Food
        fields = ['id', 'food', 'hotfoods']

class RotatingSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True)

    class Meta:
        model = Rotating
        fields = ['id', 'rotation','special', 'foods']


class CommandSerializer(serializers.ModelSerializer):
    rotatings = RotatingSerializer(many=True)

    class Meta:
        model = Command
        fields = ['id', 'command', 'rotatings']

class AirCompanySerializer(serializers.ModelSerializer):
    commands = CommandSerializer(many=True)

    class Meta:
        model = AirCompany
        fields = ['id', 'name', 'commands']

class FlightSerializer(serializers.ModelSerializer):
    air_company = AirCompanySerializer(many=True)

    class Meta:
        model = Flight
        fields = ['id', 'air_company']
