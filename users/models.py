from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseUser(AbstractUser):
    birth_date = models.DateField(null=True)
    phone_number = models.CharField(max_length=255)