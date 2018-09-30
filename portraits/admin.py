from django.contrib import admin

# Register your models here.
from .models import Portrait, Category, Location


admin.site.register(Portrait)
admin.site.register(Category)
admin.site.register(Location)
