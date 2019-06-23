from django.contrib import admin
from .models import UserProfileInfo, DrinkRate, MostPopularDrinks
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(DrinkRate)
admin.site.register(MostPopularDrinks)