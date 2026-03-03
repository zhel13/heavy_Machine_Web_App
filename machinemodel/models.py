from django.db import models

from machinecategory.models import MachineCategory


# Create your models here.
class MachineModel(models.Model):
    machine_category = models.ForeignKey(MachineCategory, on_delete=models.CASCADE, related_name='categories')
    model = models.CharField(max_length=10)
    weight = models.FloatField()
    year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.model} - {self.machine_category}'
