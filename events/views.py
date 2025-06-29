from django.shortcuts import render, get_object_or_404

from .models import Show, Event
from artworks.models import Artwork
from creators.models import Artist

def show_detail(request, pk):
    show = get_object_or_404(Show, pk=pk)
    curators = show.curators.all()
    # artworks = Artwork.objects.filter(artwork__shows == pk)
    artworks = show.artwork_set.all()
    # events = Event.objects.filter(show == pk)
    events = show.event_set.all()
    return render(request, 'events/show_detail.html', {
        'show': show,
        'events': events,
        'artworks': artworks,
        'curators': curators,
    })

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {
      'event': event
    })

