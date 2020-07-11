from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout, login as auth_login
import re
from homepage.models import Movies
from homepage.models import Userdetails
from homepage.models import Mymovies
from django.core.mail import send_mail
# Create your views here.


def index(request):

    if request.user.is_authenticated:
        movies = Movies.objects.all()
        current_user = request.user
        wallet = Userdetails.objects.filter(
            user=current_user.id).values('Wallet')
        return render(request, './frontend/index.html', {'movies': movies, 'wallet': wallet[0]})

    return render(request, './frontend/login.html')


def login(request):

    return render(request, './frontend/login.html')


def login_post(request):
    if request.method == "POST":
        if not 'email' in request.POST.keys():
            messages.error(request, "Email is missing")
            return redirect("frontend.login")

        if not 'password' in request.POST.keys():
            messages.error(request, "Password is missing")
            return redirect("frontend.login")

        email = request.POST['email']
        password = request.POST['password']

        if not re.match(r"^[\w\.\+\-\_]+\@[\w-]+\.[a-z]{2,3}$", email):
            messages.error(request, "Enter a valid Email!")
            return redirect('frontend.login')
        if len(password) < 4:
            messages.error(request, "Password is Too Short")
            return redirect('frontend.login')

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(email=email)

            if user.check_password(password):
                auth_login(request, user)
                return redirect('frontend.index')
            else:
                messages.error(request, "Invalid Password")
                return redirect('frontend.login')

        except UserModel.DoesNotExist:
            messages.error(request, "Invalid Email Please Register !")
            return redirect('frontend.login')
    else:
        messages.error(request, "Invalid Token")
        return redirect('frontend.login')


@login_required(login_url='frontend.login')
def logout_post(request):
    logout(request)
    return redirect('frontend.index')


def book(request):

    if request.user.is_authenticated:
        movie = request.POST.get('key')
        # print(movie)
        movie_selected = Movies.objects.filter(
            movie_name=movie)
        # print(movie_selected)
        current_user = request.user
        wallet = Userdetails.objects.filter(
            user=current_user.id).values('Wallet')
        return render(request, './frontend/book.html', {'columns': range(1, 8), 'rows': range(7), 'movies': movie_selected[0], 'wallet': wallet[0]})

    return render(request, './frontend/login.html')


def price(request):

    if request.user.is_authenticated:
        movie = request.POST.get('key')
        tickets = request.POST.get('tickets')
        movie_select = Movies.objects.filter(
            movie_name=movie)

        movie_rate = Movies.objects.filter(
            movie_name=movie).values('Rate')

        Total_rate = str(int(movie_rate[0]['Rate']) * int(tickets))
        # print(Total_rate)
        current_user = request.user
        wallet = Userdetails.objects.filter(
            user=current_user.id).values('Wallet')

        if int(Total_rate) > int(wallet[0]['Wallet']):
            messages.error(request, "Wallet Has less Money")
            return render(request, './frontend/book.html', {'price': Total_rate, 'movies': movie_select[0], 'wallet': wallet[0]})

        return render(request, './frontend/price.html', {'price': Total_rate, 'movies': movie_select[0], 'wallet': wallet[0]})

    return render(request, './frontend/login.html')


def price_post(request):

    if request.user.is_authenticated:
        if request.method == "POST":
            movie = request.POST.get('key')
            movie_id = request.POST.get('movie_id')
            tickets = request.POST.get('tickets')
            total = request.POST.get('total')
            movie_select = Movies.objects.filter(
                movie_name=movie)
            current_user = request.user
            wallet = Userdetails.objects.filter(
                user=current_user.id).values('Wallet')

            movie_rate = Movies.objects.filter(
                movie_name=movie).values('Rate')

            tickets = str(int(total) // int(movie_rate[0]['Rate']))

            user = User.objects.get(id=current_user.id)
            movies = Movies.objects.get(id=movie_id)

            mymovies = Mymovies(user=user,
                                movies=movies, tickets=tickets)

            mymovies.save()

            Change = Userdetails.objects.filter(
                user=current_user.id)

            if not Change:
                messages.error(request, "Login to Continue!")
                return redirect('frontend.index')

            else:
                Change = Change.get()

            Remaining = str(int(wallet[0]['Wallet'])-int(total))

            # print(Remaining)

            send_mail(
                'Booking Confirmed',
                "Movie : " + movies.movie_name + "\nDate : " +
                movies.date + "\nScreenNo : " + movies.screen +
                "\nRemainingAmount : " + Remaining,
                'bookmovietickets123@gmail.com',
                [user.email],
                fail_silently=False,
            )

            Change.Wallet = Remaining

            Change.save()

            return render(request, './frontend/success.html', {'remaining': Remaining, 'movies': movie_select[0], 'wallet': wallet[0]})
        else:
            return redirect('frontend.index')

    return render(request, './frontend/login.html')


def mymovies(request):

    if request.user.is_authenticated:
        current_user = request.user
        movies = Mymovies.objects.filter(user_id=current_user.id)
        # for i in movies:
        #     print(i.movies.date)
        wallet = Userdetails.objects.filter(
            user=current_user.id).values('Wallet')
        return render(request, './frontend/mymovies.html', {'movies': movies, 'wallet': wallet[0]})

    return render(request, './frontend/login.html')
