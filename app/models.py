from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site=models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
 
    def __str__(self):
        return self.user.username

class Drink(models.Model):
    name = models.CharField(max_length=30)

class DrinkRate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #TODO on_delete przemyśleć
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    rate= models.IntegerField()