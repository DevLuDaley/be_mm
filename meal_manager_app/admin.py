from django.contrib import admin

from .models import Meal, Recipe, Ingredient, IngredientList
# from .models import Recipe
# from .models import IngredientList
# from .models import Ingredient

admin.site.register(Meal)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(IngredientList)