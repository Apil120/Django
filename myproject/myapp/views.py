from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def helloworld(request):
    context = {
        "message":"Hello From Template"
    }
    return render(request,"hello.html",context)