from rest_framework import serializers
# from django.contrib.auth.models import Meal, Recipe

from ..models import Meal, Recipe, Ingredient, IngredientList
# from ..models import Recipe
# from ..models import IngredientList
# from ..models import Ingredient

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class IngredientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientList
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'