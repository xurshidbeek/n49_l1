from django.shortcuts import render


def index(request):
    return render(request, 'temp_1.html')
# Create your views here.

def profile(request):
    return render(request, 'profile.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def contact(request):
    return render(request, 'contacts.html')

def products(request):
    return render(request, 'products.html')