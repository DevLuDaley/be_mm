from rest_framework import routers

from ..models import Meal
from ..models import Recipe
from ..models import IngredientList
from ..models import Ingredient
# from ..frontend import Ingredient

from .views import MealViewSet, RecipeViewSet, IngredientViewSet, IngredientListViewSet

# router = routers.DefaultRouter()
# router.register(r'meals/', MealViewSet)
# router.register('api/recipes', RecipeViewSet, 'recipes')
# router.register('api/ingredients', IngredientViewSet, 'ingredients')
# router.register('api/ingredientlists', IngredientListViewSet, 'ingredientlists')
# router.register('<The URL prefix>', <The viewset class>, '<The URL name>')

# urlpatterns = router.urls