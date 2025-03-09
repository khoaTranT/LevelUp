from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# TEMP don't require csrf
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return HttpResponse("This is the accounts index.")

@csrf_exempt
def register(request):
    user = User.objects.create_user(
        request.POST['username'], "", request.POST['password'])
    return HttpResponse("Account created.")

@csrf_exempt
def login(request):
    user = authenticate(username=request.POST['username'],
                        password=request.POST['password'])
    if user is None:
        return HttpResponse("Login failed.")
    else:
        return HttpResponse("Login successful.")
