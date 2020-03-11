from django.shortcuts import render

# Create your views here.

def upcoming_movies_list(request):
	return render(request, 'upcoming_movies_list.html', {})

def movie_details(request):
	return render(request, 'movie_details.html', {})