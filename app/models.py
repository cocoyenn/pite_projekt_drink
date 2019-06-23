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
    drink_name = models.CharField(default="non",max_length=100)
    rate = models.IntegerField(null=True)

    @classmethod
    def create(cls, user, drink_name, rate):
        drink_rate = cls(user=user, drink_name = drink_name, rate=rate)
        return drink_rate

class MostPopularDrinks(models.Model):
    drink_name = models.CharField(default="non",max_length=100)
    rate_count = models.IntegerField(null=True)
    rate_sum = models.IntegerField(null=True)
    rate_avarage = models.FloatField(null=True)
    
    @classmethod
    def create(cls, drink_name, rate):
        drink_statistics = cls(drink_name = drink_name, rate_count=1, rate_sum=rate,rate_avarage=rate)
        return drink_statistics
    
    def update(self, rate):
        self.rate_count += 1
        self.rate_sum += rate
        self.rate_avarage = self.rate_sum / self.rate_count    