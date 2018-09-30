from django.shortcuts import render

from .models import Portrait
# Create your views here.


def welcome(request):

    portraits = Portrait.get_all()

    return render(request, 'portraits/home.html', {'portraits': portraits})
