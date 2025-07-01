from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

class ShowListView(LoginRequiredMixin, ListView):
    model = Show
    template_name = "events/show_list.html"

class ShowDetailView(LoginRequiredMixin, DetailView):
    model = Show
    template_name = "events/show_detail.html"

class ShowUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    def test_func(self):
        obj = self.get_object()
        for curator in obj.curators:
            if curator.user == self.request.user:
                return True
        return False

class ShowDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Show
    template_name = "events/show_delete.html"
    success_url = reverse_lazy("events:show_list")

    def test_func(self):
        obj = self.get_object()
        for curator in obj.curators.all():
            if curator.user == self.request.user:
                return True
        return False

class ShowCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
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

    def test_func(self):
        return self.request.user.groups.filter(name='curator').exists()

    # # TODO: need to make artist
    # def form_valid(self, form):
    #     form.instance.curators = [ self.request.user ]
    #     return super().form_valid(form)

class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "events/event_list.html"

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = "events/event_detail.html"

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    def test_func(self):
        obj = self.get_object()
        for curator in obj.show.curators.all():
            if curator.user == self.request.user:
                return True
        return False

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = "events/event_delete.html"
    success_url = reverse_lazy("events:event_list")

    def test_func(self):
        obj = self.get_object()
        for curator in obj.show.curators.all():
            if curator.user == self.request.user:
                return True
        return False

class EventCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
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
    
    def test_func(self):
        return self.request.user.groups.filter(name='curator').exists()


