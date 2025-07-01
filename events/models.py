from django.db import models
from creators.models import Artist
from django.urls import reverse

class Show(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='show_images', blank=True, null=True)
    curators = models.ManyToManyField(Artist)
    start = models.DateField()
    end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["start"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("events:show_detail", kwargs={"pk": self.pk})

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    show = models.ForeignKey(Show, related_name="events", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='show_images', blank=True, null=True)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("events:event_detail", kwargs={"pk": self.pk})
