from django.urls import path

from .views import (
    ArtworkListView,
    ArtworkDetailView,
    ArtworkUpdateView,
    ArtworkDeleteView,
    ArtworkCreateView,
    )

app_name = 'artworks'

urlpatterns = [
    path('', ArtworkListView.as_view(), name='artwork_list'),
    path('<int:pk>/', ArtworkDetailView.as_view(), name='artwork_detail'),
    path('<int:pk>/edit/', ArtworkUpdateView.as_view(), name='artwork_edit'),
    path('<int:pk>/delete/', ArtworkDeleteView.as_view(), name='artwork_delete'),
    path('new/', ArtworkCreateView.as_view(), name='artwork_new'),
]    
