from django.test import TestCase
from django.contrib.auth.models import User
from .models import OysReviewType, Movie, Review
import datetime
from .forms import MovieForm

# Create your tests here.

class OysReviewTest(TestCase):
    def setUp(self):
        self.type=OysReviewType(typename='Documentary')
        
    def test_typestring(self):
        self.assertEqual(str(self.type), 'Documentary')

    def test_tablename(self):
        self.assertEqual(str(OysReviewType._meta.db_table), 
        'OysReviewType')
    
class MovieTest(TestCase):
    def setUp(self):
        self.type = OysReviewType(typename='Documentary')
        self.User = User(username = 'user1')
        self.movie = Movie(moviename = 'How To Become a Tyrant', 
        movietype = self.type, user = self.User, 
        datepremiered =datetime.date(2012,5,4), 
        movieurl = 'https://www.netflix.com',
        description = 'A wonderful documentary movie')

    def test_string(self):
        self.assertEqual(str(self.movie),'How To Become a Tyrant')

class NewMovieForm(TestCase):
    def test_movieform(self):
        data = {
                'moviename' : 'The Avenger',
                'movietype': 'Super-heroes', 
                'user': 'oyster_tran',
                'dateentered': '2022-5-7',
                'producturl': 'https://www.disneyplus.com',
                'description':'A good action movie'
            }
        form = MovieForm (data)
        self.assertTrue(form.is_valid)