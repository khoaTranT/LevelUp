from django.contrib import admin

from .models import Meal

# Just allow admins to manually input new meals/ingredients.
# Might not be useful for Meal.
admin.site.register(Meal)
