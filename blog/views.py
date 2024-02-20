from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    print("blog")
    return HttpResponse("blog 1")

def blog2(request):
    print("blog2")
    return HttpResponse("blog 2")