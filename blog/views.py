from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def blog(request):
    print("blog")
    return render(request,"blog/blog.html")
