# MealsViewSet
from rest_framework import viewsets

# from .serializers import *
from .serializers import MealSerializer, RecipeSerializer, IngredientSerializer, IngredientListSerializer

from ..models import Meal, Recipe, IngredientList,Ingredient
# from .serializers import RecipeSerializer
# from .serializers import IngredientSerializer
# from .serializers import IngredientListSerializer
# from meals.models import Meal

# from django.contrib.auth.models import Meal, Recipe

# from ..models import Recipe
# from ..models import IngredientList
# from ..models import Ingredient


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientListViewSet(viewsets.ModelViewSet):
    queryset = IngredientList.objects.all()
    serializer_class = IngredientListSerializer