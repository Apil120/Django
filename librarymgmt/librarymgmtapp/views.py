from django.shortcuts import render 
from librarymgmt.settings import BASE_DIR
from .forms import Userform
# Create your views here.
def landing(request):
    print(BASE_DIR)
    return render(request,rf"{BASE_DIR}\templates\index.html")


def signin(request):
    if not request.method == "GET":
        return

    form = Userform()
    return render(request,rf"{BASE_DIR}\templates\login.html",{"form":form})
    

def signup(request):
    return render(request,rf"{BASE_DIR}\templates\signup.html")