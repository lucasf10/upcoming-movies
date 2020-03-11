import requests

from django.shortcuts import render
from django.http import JsonResponse
from requests.exceptions import HTTPError
from upcomingMovies.settings import TMDB_KEY

def get_upcoming_movies(request):
	page_number = request.GET.get('page') or '1'

	response = requests.get("http://api.themoviedb.org/3/movie/upcoming?api_key="+TMDB_KEY+"&page="+page_number)

	movies_data = get_useful_movies_data(response.json().get('results'))

	return JsonResponse({'movies': movies_data}, status=200)

def get_movie_detail(request, movie_id):
	response = requests.get("http://api.themoviedb.org/3/movie/"+str(movie_id)+"?api_key="+TMDB_KEY)

	movie_detail_data = get_useful_movie_detail_data(response.json())

	return JsonResponse({'movie_detail_data': movie_detail_data}, status=200)

def get_movie_genres():
	genres_list = requests.get("http://api.themoviedb.org/3/genre/movie/list?api_key="+TMDB_KEY)
	return genres_list.json().get('genres')

def get_useful_movies_data(raw_movie_data):
	movies_data = []

	genres_name = get_movie_genres()

	for movie in raw_movie_data:
		movies_data.append(
			{
				'id': movie.get('id'),
				'title': movie.get('title'),
				'poster_path': movie.get('poster_path'),
				'genres': [genre['name'] for genre in genres_name if genre['id'] in movie.get('genre_ids')],
				'release_date': movie.get('release_date')
			}
		)

	return movies_data

def get_useful_movie_detail_data(raw_movie_detail_data):
	movies_data =  {
		'title': raw_movie_detail_data.get('title'),
		'poster_path': raw_movie_detail_data.get('poster_path'),
		'genres': [genre['name'] for genre in raw_movie_detail_data.get('genres')],
		'release_date': raw_movie_detail_data.get('release_date'),
		'overview': raw_movie_detail_data.get('overview')
	}

	return movies_data
