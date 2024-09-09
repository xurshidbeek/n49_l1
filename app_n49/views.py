from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'temp_1.html',
                  {'posts': posts})

def profile(request):
    return render(request, 'profile.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def contact(request):
    return render(request, 'contacts.html')

def products(request):
    return render(request, 'products.html')
