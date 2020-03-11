from django.urls import path
from . import views

urlpatterns = [
    path('', views.upcoming_movies_list, name='upcoming_movies_list'),
]