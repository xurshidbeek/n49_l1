from django.urls import path
from .views import uz, rus, en, week
urlpatterns = [
    path('uz/', uz, name='uz'),
    path('rus/', rus, name='ru'),
    path('en/', en, name='en'),
    path('', week, name='week')


]