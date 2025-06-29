from django.urls import path

from .views import (
    ArtistListView,
    ArtistDetailView,
    ArtistUpdateView,
    ArtistDeleteView,
    ArtistCreateView,
    )

app_name = 'creators'

urlpatterns = [
    path('', ArtistListView.as_view(), name='artist_list'),
    path('<int:pk>/', ArtistDetailView.as_view(), name='artist_detail'),
    path('<int:pk>/edit/', ArtistUpdateView.as_view(), name='artist_edit'),
    path('<int:pk>/delete/', ArtistDeleteView.as_view(), name='artist_delete'),
    path('new/', ArtistCreateView.as_view(), name='artist_new'),
]    
