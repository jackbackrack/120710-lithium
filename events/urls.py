from django.urls import path

from .views import (
    ShowListView,
    ShowDetailView,
    ShowUpdateView,
    ShowDeleteView,
    ShowCreateView,
    EventListView,
    EventDetailView,
    EventUpdateView,
    EventDeleteView,
    EventCreateView,
    )

app_name = 'events'

urlpatterns = [
    path('show/', ShowListView.as_view(), name='show_list'),
    path('show/<int:pk>/', ShowDetailView.as_view(), name='show_detail'),
    path('show/<int:pk>/edit/', ShowUpdateView.as_view(), name='show_edit'),
    path('show/<int:pk>/delete/', ShowDeleteView.as_view(), name='show_delete'),
    path('show/new/', ShowCreateView.as_view(), name='show_new'),
    path('event/', EventListView.as_view(), name='event_list'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event/<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('event/new/', EventCreateView.as_view(), name='event_new'),
]    
