from django.db import models
from .trip import Trip

class Item(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
