from django.shortcuts import get_list_or_404

from .models import Ingredient
from .serializers import IngredientsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def profile(request):
    pass


@api_view(['GET'])
def ingredients(request):
    ingredients = get_list_or_404(Ingredient)
    serializer = IngredientsSerializer(ingredients, many=True)
    return Response(serializer.data)


def ingredient_add_delete(request, ingredient_pk):
    pass
