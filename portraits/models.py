import datetime as dt

from django.db import models


class Location(models.Model):

    location = models.CharField(max_length=60, blank=True)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_loaction(self, update):
        self.anime_loaction = update
        self.save()

    def __str__(self):
        return self.location

    @classmethod
    def get_all_locations(cls):
        locations = Location.objects.all()
        return locations


class Category(models.Model):

    category = models.CharField(max_length=60, blank=True)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, update):
        self.anime_category = update
        self.save()

    @classmethod
    def get_all_category(cls):
        category = Category.objects.all()
        return category

    def __str__(self):
        return self.category


class Portrait(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def save_portrait(self):
        self.save()

    def delete_portrait(self):
        self.delete()

    def update_portrait(self, update):
        self.anime_portrait = update
        self.save()

    @classmethod
    def get_all(cls):
        portraits = Portrait.objects.all()
        return portraits

    @classmethod
    def find_by_location(cls, location):
        portrait = Portrait.objects.filter(location__location=location)
        return portrait

    @classmethod
    def find_by_category(cls, category):
        category = Portrait.objects.filter(category__category=category)
        return category

    @classmethod
    def search_by_name(cls, anime):
        portrait = Portrait.objects.filter(name_icontains=anime)
        return portrait

    def __str__(self):
        return self.name
