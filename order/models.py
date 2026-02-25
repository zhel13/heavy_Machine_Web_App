from decimal import Decimal
from tkinter.constants import CASCADE

from django.core.validators import MinValueValidator
from django.db import models

from common.models import TimeStamp
from part.models import Part
from user_profile.models import Profile


# Create your models here.
class Order(TimeStamp):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders')
    part = models.ManyToManyField(Part)
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    is_completed = models.BooleanField(default=False)