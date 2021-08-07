from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def task(request):
    return render(request, 'main/task.html')


def price(request):
    return render(request, 'main/price.html')


def cars(request):
    return render(request, 'main/cars.html')
