from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Artwork

class ArtworkListView(ListView):
    model = Artwork
    template_name = "artworks/artwork_list.html"

class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = "artworks/artwork_detail.html"

class ArtworkUpdateView(UpdateView):
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

class ArtworkDeleteView(DeleteView):
    model = Artwork
    template_name = "artworks/artwork_delete.html"
    success_url = reverse_lazy("artwork_list")

class ArtworkCreateView(CreateView):
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


