from django.shortcuts import render, redirect
from django.contrib import messages
# from django.db.models import Count
from .models import User
from ..book_reviews.models import Review

def index(request):

    if 'user' in request.session:

        return redirect('book_reviews:index')

    else:

        return render(request, 'login_registration/index.html')


def create(request):

    if request.method != 'POST':

        return redirect('login_registration:index')

    else:

        response = User.objects.validate_registration(request.POST)

        if response[0] == False:
            for message in response[1]:
                messages.error(request, '*' + message[0], extra_tags=message[1])

            return redirect('login_registration:index')

        else:

            request.session['user'] = {

                'id': response[1]['id'],
                'name': response[1]['name'],
                'alias': response[1]['alias'],
                'email': response[1]['email']
            }


        return redirect('login_registration:index')


def login(request):

    if request.method != 'POST':

        return redirect('login_registration:index')

    else:

        response = User.objects.validate_login(request.POST)

        if response[0] == False:

            for message in response[1]:
                messages.error(request, '*' + message, 'login')

                return redirect('login_registration:index')

        else:

            request.session['user'] = {

                'id': response[1]['id'],
                'name': response[1]['name'],
                'alias': response[1]['alias'],
                'email': response[1]['email']

            }

            return redirect('login_registration:index')


def logout(request):

    request.session.clear()

    return redirect('login_registration:index')


def user_reviews(request, id):

    try:

        user = User.objects.get(id=id)

        context = {

            'user': {
                'name': user.name,
                'alias': user.alias,
                'email': user.email,
            },
            'user_reviews': Review.objects.filter(user=user).order_by('book__title'),
            'count_reviews': Review.objects.filter(user=user).count()

        }

        return render(request, 'login_registration/user_reviews.html', context)

    except:

        return redirect('book_reviews:index')
