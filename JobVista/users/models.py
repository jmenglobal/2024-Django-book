from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    founded_in = models.PositiveIntegerField(null=True, blank=True) # Year the user was founded\

  # 'null=True' allows the field to be empty in the database (it can have a null value).
# 'blank=True' means that the field is not required in forms (it can be left empty by the user).
  