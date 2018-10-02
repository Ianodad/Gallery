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

    category = Category.get_all_category()

    portrait = Portrait.find_by_location(location)

    return render(request, "portraits/location.html", {"portrait": portrait, "locations": locations, "category": category})


def category(request, category):
    categories = Category.get_all_category()

    locations = Location.get_all_locations()

    portrait = Portrait.find_by_category(category)

    # print(portrait)
    return render(request, "portraits/category.html", {"categories": categories, "portrait": portrait, "locations": locations})


def search(request):

    if 'portrait' in request.GET and request.GET["portrait"]:
        search_anime = request.GET.get("portrait")
        searched = Portrait.search_by_name(search_anime)
        message = f"{searched_name}"

        return render(request, 'portraits/search.html', {"message": message, "portrait": searched})

    else: 
        message = "You havent searched for any term"

        return render(request, "portraits/search.html", {"message":message })
