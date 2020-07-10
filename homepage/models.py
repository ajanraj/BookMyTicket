from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Movies(models.Model):

    movie_name = models.CharField(max_length=50)
    poster_link = models.CharField(
        max_length=1000, default='https://xl.movieposterdb.com/19_12/2017/3890160/xl_3890160_081e65b0.jpg')
    date = models.CharField(max_length=50)
    screen = models.CharField(max_length=20)
    Rate = models.CharField(max_length=20)

    def __str__(self):
        return self.movie_name


class Userdetails(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Wallet = models.CharField(default=50, max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.Wallet


class Mymovies(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ForeignKey(Movies, on_delete=models.CASCADE)
    tickets = models.CharField(max_length=20)

    def __str__(self):
        return self.movies.movie_name
