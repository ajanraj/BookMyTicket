from django.contrib import admin
from .models import Movies, Userdetails, Mymovies
# Register your models here.

admin.site.register(Movies)
admin.site.register(Userdetails)
admin.site.register(Mymovies)
