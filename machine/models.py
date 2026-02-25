from django.db import models

# Create your models here.
class Machine(models.Model):
    category = models.CharField(
        max_length=100
    )
    model = models.CharField(max_length=100)
    weight = models.IntegerField()
    year = models.IntegerField()

