from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from common.models import TimeStamp


# Create your models here.
class Profile(TimeStamp):
    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2),
        ]
    )
    email = models.EmailField()
    phone = models.CharField(
        max_length=15,
    )
    address = models.CharField(
        max_length=100,
    )
    city = models.CharField(
        max_length=100,
    )
    is_active = models.BooleanField(
        default=True,
    )