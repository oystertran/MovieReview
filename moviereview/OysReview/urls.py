from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('movies/',views.movies, name='movies'),
    path('moviedetail/<int:id>', views.movieDetail, 
    name = 'detail'),
    path('newmovie', views.newMovie, name = 'newmovie'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]