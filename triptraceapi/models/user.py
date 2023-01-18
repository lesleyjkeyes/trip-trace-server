from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=50)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    about = models.CharField(max_length=400)
    image_url = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
