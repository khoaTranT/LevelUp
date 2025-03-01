from django.urls import path, include
from meals import views

urlpatterns = [
    path('meal/', views.MealList.as_view()),
]
