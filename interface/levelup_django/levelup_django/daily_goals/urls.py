from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_api_urls, name='get_api_urls'),
    path('goalList/', views.goalList, name='goalList'),
    path('calories/<str:pk>', views.getCalories, name='calories'),
    path('calculateCalories/<str:pk>', views.calculateCalories, name='calculateCalories'),
    path('weight/<str:pk>', views.weightGoal, name='weight'),
    path("steps/<str:pk>", views.stepsGoal, name="steps"),
    path("dailySteps/<str:pk>", views.getDailySteps, name="dailySteps"),
    path("weightGoal/<str:pk>", views.getWeightGoal, name="weightGoal"),
    path("getUserId/", views.get_user_id, name="getUserId"),
    path("updateCalories/<str:pk>", views.updateDailyCalories, name="updateCalories"),
    path("createDailyGoals/", views.createDailyGoals, name="createDailyGoals"),
    path("searchMeals/", views.search_meal_list, name="searchMeals")
    

    
]