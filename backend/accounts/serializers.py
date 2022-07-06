from .models import Fridge, Ingredient
from rest_framework import serializers
from django.contrib.auth import get_user_model


class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'ingredients')

