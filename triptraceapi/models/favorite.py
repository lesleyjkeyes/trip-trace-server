from django.db import models
from .trip import Trip
from .user import User

class Favorite(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    traveler = models.ForeignKey(User, on_delete=models.CASCADE)
