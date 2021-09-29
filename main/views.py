from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


# Create your views here.


def index(request):
    return render(request, 'main/index.html' )

def forum(request):
    news = Post.objects.order_by("-date")
    return render(request, 'main/forum.html', {'news':news})

def task(request):
    return render(request, 'main/task.html')


def price(request):
    return render(request, 'main/price.html')


def cars(request):
    return render(request, 'main/cars.html')
