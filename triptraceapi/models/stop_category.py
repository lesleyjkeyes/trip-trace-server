from django.db import models
from .stop import Stop
from .category import Category

class StopCategory(models.Model):
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
