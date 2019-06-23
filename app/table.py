import django_tables2 as tables
from .models import DrinkRate, MostPopularDrinks
class DrinkRateTable(tables.Table):
    class Meta:
        model = DrinkRate
        fields = ('rate', 'drink_name') 

class MostPopularDrinksTable(tables.Table):
    class Meta:
        model = MostPopularDrinks
        fields = ('rate_avarage', 'drink_name') 
