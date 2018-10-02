from django.shortcuts import render

from .models import Portrait, Location, Category
# Create your views here.


def welcome(request):

    portraits = Portrait.get_all()

    locations = Location.get_all_locations()

    return render(request, "portraits/home.html", {"portraits": portraits, "locations": locations})


def location(request, location):
    locations = Location.get_all_locations()

    portrait = Portrait.find_by_location(location)

    return render(request, "portraits/location.html", {"portrait": portrait, "locations": locations})


def category(request, category):
    category = Category.get_all_category()

    portrait = Portrait.find_by_category(category)

    return render(request, "portraits/category.html", {"category": category, "portrait": portrait})


def search(request):

    return render(request, "portraits/location.html", {})
