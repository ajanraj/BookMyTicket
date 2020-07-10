from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='frontend.index'),
    path('login', views.login, name='frontend.login'),
    path('login/post', views.login_post, name='frontend.login.post'),
    path('logout/', views.logout_post, name='frontend.logout'),
    path('book/', views.book, name='frontend.book'),
    path('price/', views.price, name='frontend.price'),
    path('success/', views.price_post, name='frontend.price_post'),
    path('mymovies/', views.mymovies, name='frontend.mymovies'),

]
