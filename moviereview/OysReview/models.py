from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class OysReviewType(models.Model):
    typename = models.CharField(max_length = 255)
    typedescription = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.typename
    class Meta:
        db_table = 'OysReviewType'

class Movie(models.Model):
    moviename = models.CharField(max_length = 255)
    movietype = models.ForeignKey(OysReviewType, on_delete = models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    datepremiered = models.DateField()
    movieurl = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.moviename

    class Meta:
        db_table = 'movie'

class Review(models.Model):
    title = models.CharField(max_length = 255)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    reviewdate = models.DateField()
    reviewtext = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'review'