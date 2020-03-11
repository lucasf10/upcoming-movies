from django.urls import path
from . import views

urlpatterns = [
    path('get_upcoming_movies', views.get_upcoming_movies, name='get_upcoming_movies'),
]