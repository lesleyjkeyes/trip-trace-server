from django.db import models
from .trip import Trip
from .country import Country

class Stop(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    duration = models.IntegerField()
    duration_unit = models.CharField(max_length=25)
    price_range = models.CharField(max_length=50)
    