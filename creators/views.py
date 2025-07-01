from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Artist

class ArtistListView(LoginRequiredMixin, ListView):
    model = Artist
    template_name = "artists/artist_list.html"

class ArtistDetailView(LoginRequiredMixin, DetailView):
    model = Artist
    template_name = "artists/artist_detail.html"

class ArtistUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

class ArtistDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Artist
    template_name = "artists/artist_delete.html"
    success_url = reverse_lazy("creators:artist_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

class ArtistCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
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

    def form_valid(self, form):
        form.instance.user = self.request.user
        print('user set to', self.request.user)
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.groups.filter(name='artist').exists()

# from django.shortcuts import render, get_object_or_404
# 
# def artist_list(request):
#     artist = get_object_or_404(Artist, pk=pk)
#     return render(request, 'creators/artist_detail.html', {
#       'artist': artist
#     })

