from django.db import models
from .user import User

class Trip(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(max_length=10)
    duration_unit = models.CharField(max_length=25)
    traveler = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    public = models.BooleanField(default=False)
    price_range = models.CharField(max_length=10)
    