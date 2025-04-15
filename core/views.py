# from django.shortcuts import render
# def home(request):
# 	return render(request, 'core/index.html')

from django.views.generic import ListView
from .models import Movie


class MovieListView(ListView):
	model = Movie
	template_name = 'core/index.html'
	context_object_name = 'movies'
