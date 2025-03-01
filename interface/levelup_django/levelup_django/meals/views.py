from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Meal
from .serializers import MealSerializer
# Create your views here.
# TODO: Implement fetching data from the CDU database
class MealList(APIView):
    def get(self, request, format=None):
        meals = Meal.objects.all() [0:5]
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)
