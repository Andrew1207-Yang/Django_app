from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from blog.models import Post

def home(request):
    obj = get_object_or_404(Post, id = 33)
    context = {
        'object':obj,
    }
    return render(request,"home.html",context)

def about(request):
    return render(request, "about_us.html",{})

def more(request):
    return render(request, "more.html",{})

def product(request):
    return render(request, "coming_soon.html",{})