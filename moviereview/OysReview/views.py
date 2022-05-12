from django.shortcuts import render, get_object_or_404
from .models import Movie, OysReviewType, Review
from django.urls import reverse_lazy
from .forms import MovieForm
from django.contrib.auth.decorators import login_required

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

@login_required

def newMovie(request):
    form = MovieForm

    if request.method =='POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = MovieForm
    else:
        form = MovieForm()
    return render(request,'oysreview/newmovie.html',
    {'form':form})

def loginmessage(request):
    return render(request, 'OysReview/loginmessage.html')

def logoutmessage(request):
    return render(request, 'OysReview/logoutmessage.html')