from django.shortcuts import get_list_or_404
from django.contrib.auth import get_user_model

from .models import Ingredient
from .serializers import IngredientsSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

User = get_user_model()

@api_view(['GET'])
def profile(request):
    user = request.user
    print(user)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def ingredients(request):
    ingredients = get_list_or_404(Ingredient)
    serializer = IngredientsSerializer(ingredients, many=True)
    return Response(serializer.data)


def ingredient_add_delete(request, ingredient_pk):
    pass
