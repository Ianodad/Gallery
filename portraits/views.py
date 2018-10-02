from django.shortcuts import render

from .models import Portrait, Location, Category
# Create your views here.


def welcome(request):

    portraits = Portrait.get_all()

    category = Category.get_all_category()

    locations = Location.get_all_locations()

    return render(request, "portraits/home.html", {"portraits": portraits, "locations": locations, "category": category})


def location(request, location):
    locations = Location.get_all_locations()

    portrait = Portrait.find_by_location(location)

    return render(request, "portraits/location.html", {"portrait": portrait, "locations": locations})


def category(request, category):
    categories = Category.get_all_category()
    # category = "Hi"

    portrait = Portrait.find_by_category(category)

    # print(portrait)
    return render(request, "portraits/category.html", {"categories": categories, "portrait": portrait})


def search(request):

    return render(request, "portraits/search.html", {})
