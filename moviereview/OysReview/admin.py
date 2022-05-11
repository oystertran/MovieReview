from django.contrib import admin
from .models import OysReviewType, Movie, Review

# Register your models here.

admin.site.register(OysReviewType)
admin.site.register(Movie)
admin.site.register(Review)