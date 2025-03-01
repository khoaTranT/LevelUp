# Responsible for creating json files to be used by Vue (for webpage layout)
from rest_framework import serializers
from .models import Meal

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = (
            "user",
            "meal_name",
            "calories",
            "macronutrients",
            "ingredients",
            "created_at"
        )