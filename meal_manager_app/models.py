from django.db import models

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=50)
    meal_type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name + ' ' + self.meal_type

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    recipe_type = models.CharField(max_length=50)
    cousine = models.CharField(max_length=50)
    ingredient_list = models.CharField(max_length=500)
    instructions = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name + ' ' + self.recipe_type

class IngredientList(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name + ' ' + self.ingredients

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    measurement = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    ingredient_list = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name + ' ' + self.measurement