from django.shortcuts import render

from creators.models import Artist
from artworks.models import Artwork
from events.models import Show, Event

def index(request):
    pieces = Artwork.objects.filter()[0:6]
    shows = Show.objects.filter().order_by('-start')
    artists = Artist.objects.filter().order_by('user__last_name')
    return render(request, 'gallery/index.html', {
        'pieces': pieces,
        'shows': shows,
        'artists': artists,
    })

