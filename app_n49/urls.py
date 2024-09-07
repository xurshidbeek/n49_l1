from django.urls import path
from .views import index, profile, dashboard, contact, products
urlpatterns = [
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('contact/', contact, name='contact'),
    path('products/', products, name='product'),
]