from django.db import models
from .trip import Trip

class Stop(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    duration = models.IntegerField()
    duration_unit = models.CharField(max_length=25)
    price_range = models.CharField(max_length=50)
    