from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_artist = models.BooleanField(default=False)
    is_curator = models.BooleanField(default=False)

    def __str__(self):
        return self.email