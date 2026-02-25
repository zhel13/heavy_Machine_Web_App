from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import ForeignKey, SET_NULL

from common.models import TimeStamp
from machine.models import Machine


# Create your models here.
class Part(TimeStamp):
    name = models.CharField(max_length=100)
    model = ForeignKey(Machine, on_delete=SET_NULL, related_name='parts', null=True)
    serial_number = models.IntegerField(
        null=True,
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
