from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    password_change_date = models.DateTimeField(auto_now_add=True, null=True)
