from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Artist

class ArtistListView(ListView):
    model = Artist
    template_name = "artists/artist_list.html"

class ArtistDetailView(DetailView):
    model = Artist
    template_name = "artists/artist_detail.html"

class ArtistUpdateView(UpdateView):
    model = Artist
    fields = (
        "phone",
        "website",
        "instagram",
        "bio",
        "statement",
        "image",
        )
    template_name = "artists/artist_edit.html"

class ArtistDeleteView(DeleteView):
    model = Artist
    template_name = "artists/artist_delete.html"
    success_url = reverse_lazy("artist_list")

class ArtistCreateView(CreateView):
    model = Artist
    fields = (
        "phone",
        "website",
        "instagram",
        "bio",
        "statement",
        "image",
        )
    template_name = "artists/artist_new.html"

# from django.shortcuts import render, get_object_or_404
# 
# def artist_list(request):
#     artist = get_object_or_404(Artist, pk=pk)
#     return render(request, 'creators/artist_detail.html', {
#       'artist': artist
#     })

