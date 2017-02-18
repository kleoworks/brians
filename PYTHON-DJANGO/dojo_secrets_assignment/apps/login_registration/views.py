from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):

    if 'user' in request.session:

        return redirect('dojo_secrets:index')

    else:

        return render(request, 'login_registration/index.html')


def create(request):

    if request.method != 'POST':
        return redirect('login_registration:index')


    response = User.objects.validate_new_user(request.POST)

    if response[0] == False:

        for message in response[1]:
            messages.error(request, message, extra_tags='registration')

        return redirect('login_registration:index')

    else:

        request.session['user'] = {

            'id': response[1]['id'],
            'first_name': response[1]['first_name']
        }

        return redirect('login_registration:index')


def login(request):

    if request.method != 'POST':
        return redirect('login_registration:index')


    response = User.objects.validate_login(request.POST)

    if response[0] == False:

        for message in response[1]:
            messages.error(request, message, extra_tags='login')
            return redirect('login_registration:index')

    else:

        request.session['user'] = {

            'id': response[1]['id'],
            'first_name': response[1]['first_name']

        }

        return redirect('login_registration:index')


def logout(request):

    request.session.clear()
    return redirect('login_registration:index')
