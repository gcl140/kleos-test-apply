from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Official Email")
    username = models.EmailField(unique=True, blank=True, null=True)  # Use email as the username

    @property
    def is_counsellor(self):
        return hasattr(self, "coordinator")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Coordinator(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="coordinator")
    # phone_number = models.CharField(max_length=20)  # Include country code
    username = models.EmailField(unique=True, blank=True, null=True)  # Use email as the username

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - coordinator"
