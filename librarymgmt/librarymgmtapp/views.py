from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login
from django.http import JsonResponse
from librarymgmt.settings import BASE_DIR
import os
from .forms import Userform

# Create your views here.
def landing(request):
    print(os.listdir(BASE_DIR))
    return render(request,rf"{BASE_DIR}\templates\index.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("")  
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
    return render(request, "login.html")