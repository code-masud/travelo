
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumber


class User(AbstractUser):
    phone = PhoneNumber()
    avatar = models.ImageField(upload_to='avatar')
    address = models.TextField()

    class Meta:
        ordering = ["-date_joined"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
