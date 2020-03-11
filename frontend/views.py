from django.shortcuts import render

def upcoming_movies_list(request):
	return render(request, 'upcoming_movies_list.html', {})

def movie_detail(request, movie_id):
	return render(request, 'movie_detail.html', {'movie_id': str(movie_id)})
