from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    print("home")
    return HttpResponse("Home")

def home2(request):
    print("home")
    return render(request,"home/index.html")
