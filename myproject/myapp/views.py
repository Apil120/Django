from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myproject.settings import BASE_DIR
# Create your views here.
def say_hello(request,name):
    context = {"name":name}
    return render(request,rf"{BASE_DIR}\templates\helloworld.html",context=context)

def greet_user(request,name):
    return_object = {"User":name}
    return JsonResponse(return_object)