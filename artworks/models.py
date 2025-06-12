from django.db import models
from events.models import Show
from creators.models import Artist

class Artwork(models.Model):
    name = models.CharField(max_length=255)
    shows = models.ManyToManyField(Show)
    artists = models.ManyToManyField(Artist)
    end_year = models.IntegerField()
    start_year = models.IntegerField(blank=True, null=True)
    medium = models.TextField(blank=True, null=True)
    dimensions = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='piece_images', blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    pricing = models.CharField(max_length=255, blank=True, null=True)
    replacement_cost = models.FloatField(blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    installation = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


