from django.shortcuts import render, get_object_or_404
from .models import Cocktail
from django.http import HttpResponse


# pages for ex1
def index(request):
    context = {
        'name': 'home'
    }
    return render(request, 'cwApp/home.html', context)


def two(request):
    context = {
        'name': ' from home'
    }
    return render(request, 'cwApp/Page2.html', context)

def three(request):
    context = {
        'name': ' from page2'
    }
    return render(request, 'cwApp/Page3.html', context)

def four(request):
    context = {
        'name': ' from page3'
    }
    return render(request, 'cwApp/Page4.html', context)

def five(request):
    context = {
        'name': ' from page4'
    }
    return render(request, 'cwApp/Page5.html', context)


# pages for ex2
def cocktails(request):
    allDrinks = Cocktail.objects.all()
    context = {
        'drinks': allDrinks
    }
    return render(request, 'cwApp/cocktail.html', context)


def details(request, drinkID):
    drinks = get_object_or_404(Cocktail, pk=drinkID)
    context = {
        'drink': drinks
    }
    return render(request, 'cwApp/details.html', context)

