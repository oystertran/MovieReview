from django import forms 
from .models import OysReviewType, Movie, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'