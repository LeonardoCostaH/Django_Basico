from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    print("home")
    print("minha página home é completona!!")
    return HttpResponse("home teste")

