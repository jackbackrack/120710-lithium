from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Artwork

class ArtworkListView(LoginRequiredMixin, ListView):
    model = Artwork
    template_name = "artworks/artwork_list.html"

class ArtworkDetailView(LoginRequiredMixin, DetailView):
    model = Artwork
    template_name = "artworks/artwork_detail.html"

class ArtworkUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Artwork
    fields = (
        "name",
        "shows",
        "artists",
        "end_year",
        "start_year",
        "medium",
        "dimensions",
        "image",
        "price",
        "pricing",
        "replacement_cost",
        "is_sold",
        "description",
        "installation",
        )
    template_name = "artworks/artwork_edit.html"

    def test_func(self):
        obj = self.get_object()
        for artist in obj.artists.all():
            if artist.user == self.request.user:
                return True
        return self.request.user.is_superuser

class ArtworkDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Artwork
    template_name = "artworks/artwork_delete.html"
    success_url = reverse_lazy("artworks:artwork_list")

    def test_func(self):
        obj = self.get_object()
        for artist in obj.artists.all():
            if artist.user == self.request.user:
                return True
        return self.request.user.is_superuser

class ArtworkCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Artwork
    fields = (
        "name",
        "shows",
        "artists",
        "end_year",
        "start_year",
        "medium",
        "dimensions",
        "image",
        "price",
        "pricing",
        "replacement_cost",
        "is_sold",
        "description",
        "installation",
        )
    template_name = "artworks/artwork_new.html"

    # # todo: artist with this user id
    # def form_valid(self, form):
    #     form.instance.artists = [ self.request.user ]
    #     return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='artist').exists()

