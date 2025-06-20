from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Official Email")
    username = models.EmailField(unique=True, blank=True, null=True)  # Use email as the username
    is_intern = models.BooleanField(default=False, blank=True, null=True)  # Add the internship field


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class ApplicationSettings(models.Model):
    is_portal_open = models.BooleanField(default=True)

    def __str__(self):
        return "Portal Open" if self.is_portal_open else "Portal Closed"

    @classmethod
    def get_state(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
