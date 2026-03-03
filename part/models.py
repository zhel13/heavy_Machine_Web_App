from decimal import Decimal

from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator
from django.db import models
from django.db.models import ForeignKey
from django.utils.text import slugify

from common.models import TimeStamp
from machinecategory.models import MachineCategory
from machinemodel.models import MachineModel


# Create your models here.
class Part(TimeStamp):
    name = models.CharField(max_length=100)
    machine_compatibility = models.ManyToManyField(MachineModel)
    serial_number = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(10),
        ],
        null=True,
    )
    slug = models.CharField(
        max_length=100,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal('0.01')),
        ]
    )
    in_stock = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
        ]
    )
    is_available = models.BooleanField(
        default=False,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.serial_number}')
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
