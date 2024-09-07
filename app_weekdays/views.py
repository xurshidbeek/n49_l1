from django.shortcuts import render


def uz(request):
    return render(request, 'weekdays/uz.html')


def rus(request):
    return render(request, 'weekdays/ru.html')


def en(request):
    return render(request, 'weekdays/en.html')


def week(request):
    return render(request, 'weekdays/weekday.html')
