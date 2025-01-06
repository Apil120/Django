from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect
from myproject.settings import BASE_DIR
from .forms import BookForm
import os
# Create your views here.
def say_hello(request,name):
    context = {"name":name}
    return render(request,rf"{BASE_DIR}\templates\index.html",context=context)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

            return JsonResponse({"message":"Book saved sucessfully!"})
        
    else:
        form = BookForm()

    return render(request,"add_book.html",{"form":form})
def greet_user(request,name):
    return_object = {"user":name}
    return JsonResponse(return_object)


def landing(request):
    print(BASE_DIR)
    print(os.listdir(BASE_DIR))
    return render(request,rf"{BASE_DIR}\templates\greet.html")