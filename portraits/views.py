from django.shortcuts import render

from .models import Portrait
# Create your views here.


def welcome(request):

    name = Portrait.name

    return render(request, 'portraits/home.html')
