from django.db import models

class Country(models.Model):
    alpha2 = models.CharField(max_length=10)
    alpha3 = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
