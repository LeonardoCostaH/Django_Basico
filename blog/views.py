from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def blog(request):
    print("blog")
    return render(request,"blog_1.html")

def blog2(request):
    print("blog2")
    return render(request, 'blog.html')