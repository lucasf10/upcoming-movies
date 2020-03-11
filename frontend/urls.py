from django.urls import path
from . import views

urlpatterns = [
    path('', views.upcoming_movies_list, name='upcoming_movies_list'),
    path('search/', views.upcoming_movies_list, name='search_upcoming_movies_list'),
    path('detail/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]