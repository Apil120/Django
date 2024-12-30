from django.shortcuts import render
# Create your views here.
def say_hello(request,name):
    context = {"name":name}
    return render(request,"templates/helloworld.html",context=context)