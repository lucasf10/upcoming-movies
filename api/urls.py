from django.urls import path
from . import views

urlpatterns = [
    path('get_upcoming_movies', views.get_upcoming_movies, name='get_upcoming_movies'),
    path('get_movie_detail/<int:movie_id>/', views.get_movie_detail, name='get_movie_detail'),
]