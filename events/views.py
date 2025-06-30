from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404

from .models import Show, Event
from artworks.models import Artwork
from creators.models import Artist

def show_detail_all(request, pk):
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

class ShowListView(ListView):
    model = Show
    template_name = "events/show_list.html"

class ShowDetailView(DetailView):
    model = Show
    template_name = "events/show_detail.html"

class ShowUpdateView(UpdateView):
    model = Show
    fields = (
        "name",
        "description",
        "image",
        "curators",
        "start",
        "end",
        )
    template_name = "events/show_edit.html"

class ShowDeleteView(DeleteView):
    model = Show
    template_name = "events/show_delete.html"
    success_url = reverse_lazy("show_list")

class ShowCreateView(CreateView):
    model = Show
    fields = (
        "name",
        "description",
        "image",
        "curators",
        "start",
        "end",
        )
    template_name = "events/show_new.html"


class EventListView(ListView):
    model = Event
    template_name = "events/event_list.html"

class EventDetailView(DetailView):
    model = Event
    template_name = "events/event_detail.html"

class EventUpdateView(UpdateView):
    model = Event
    fields = (
        "name",
        "description",
        "show",
        "image",
        "date",
        "start",
        "end",
        )
    template_name = "events/event_edit.html"

class EventDeleteView(DeleteView):
    model = Event
    template_name = "events/event_delete.html"
    success_url = reverse_lazy("event_list")

class EventCreateView(CreateView):
    model = Event
    fields = (
        "name",
        "description",
        "show",
        "image",
        "date",
        "start",
        "end",
        )
    template_name = "events/event_new.html"
    