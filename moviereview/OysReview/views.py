from django.shortcuts import render, get_object_or_404
from .models import Movie, OysReviewType, Review
from django.urls import reverse_lazy

# Create your views here.

def index (request):
    return render(request, 'OysReview/index.html')

def movies(request):
    movie_list = Movie.objects.all()
    return render (request, 'OysReview/movies.html', 
    {'movie_list': movie_list})

def movieDetail (request,id):
    movie = get_object_or_404(Movie, pk = id)
    return render(request,'OysReview/moviedetail.html',
    {'movie': movie})