from django.shortcuts import render

from rest_framework import routers

from .api.views import MealViewSet, RecipeViewSet, IngredientListViewSet, IngredientViewSet
# from .api.views import RecipeViewSet
# from .api.views import IngredientViewSet
# from .api.views import IngredientListViewSet

# router = routers.DefaultRouter()
# router.register(r'meals', MealViewSet)
# router.register('meals', MealViewSet, 'meals')
# router.register('<The URL prefix>', <The viewset class>, '<The URL name>')

# urlpatterns = router.urls