from django.shortcuts import render
from librarymgmt.settings import BASE_DIR
import os

# Create your views here.
def landing(request):
    print(os.listdir(BASE_DIR))
    return render(request,rf"{BASE_DIR}\templates\index.html")