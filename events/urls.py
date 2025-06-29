from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('show/<int:pk>/', views.show_detail, name='show_detail'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
]    
