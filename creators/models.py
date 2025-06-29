from django.db import models
from django.conf import settings
from accounts.models import CustomUser
from django.urls import reverse

class Artist(models.Model):
    user = models.ForeignKey(CustomUser, related_name='accounts', on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    website = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    statement = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='artist_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["user__last_name"]

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    def get_absolute_url(self):
        return reverse("creators:artist_detail", kwargs={"pk": self.pk})
