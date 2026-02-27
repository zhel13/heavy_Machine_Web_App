from decimal import Decimal

from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator
from django.db import models
from django.db.models import ForeignKey
from django.utils.text import slugify

from common.models import TimeStamp
from machine.models import Machine


# Create your models here.
class Part(TimeStamp):
    name = models.CharField(max_length=100)
    machines = ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name='parts',
    )
    serial_number = models.IntegerField(
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
    description = models.TextField()
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
            self.slug = slugify(f'{self.name}-{self.machines.model}')
        super().save(*args, **kwargs)



