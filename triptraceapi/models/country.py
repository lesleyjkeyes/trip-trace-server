from django.db import models

class Country(models.Model):
    country_number = models.IntegerField()
    alpha2 = models.CharField(max_length=10)
    alpha3 = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
