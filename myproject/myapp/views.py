from django.shortcuts import render
from django.http import JsonResponse
from myproject.settings import BASE_DIR
# Create your views here.
def say_hello(request,name):
    context = {"name":name}
    return render(request,rf"{BASE_DIR}\templates\index.html",context=context)

def greet_user(request,name):
    return_object = {"user":name}
    return JsonResponse(return_object)

def landing(request):
    return render(request,rf"{BASE_DIR}\templates\greet.html")