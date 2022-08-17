from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

UserModel: AbstractUser = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    city = models.CharField(max_length=64, null=False, blank=True)

    def __str__(self):
        return self.user.username





