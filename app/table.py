import django_tables2 as tables
from .models import DrinkRate
class DrinkRateTable(tables.Table):
    class Meta:
        model = DrinkRate

