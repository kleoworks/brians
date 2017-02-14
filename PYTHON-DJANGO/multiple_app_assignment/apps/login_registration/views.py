from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User
from ..courses.models import Course, Description


# show main registration and login page
def index(request):

    if 'user' in request.session:

        messages.success(request, 'You appear to be still logged in...')
        return redirect('login_registration:success')



    return render(request, 'login_registration/index.html')


# show success page upon registration or login
def success(request):

    return render(request, 'login_registration/welcome.html')


# handles new user registration
def register(request):

    if request.method != 'POST':
        return redirect('login_registration:index')

    else:

        # pass form data to User validation method
        # if errors, a tuple is returned in the format ('error', [message1, message2, message3,...])
        #   redirect to registration page and show errors to user
        # if no errors, a Query object is returned with newly created user information
        #   store basic user info into session
        #   redirect to success page and show success message to user
        user = User.objects.validate_new_user(request.POST)

        if type(user) == tuple:

            # show error messages
            for message in user[1]:
                messages.error(request, message)

            return redirect('login_registration:index')

        else:

            request.session['user'] = {
                'id': user[0].id,
                'first_name': user[0].first_name,
                'last_name': user[0].last_name,
                'email': user[0].email
            }

            messages.success(request, 'Successfully registered!')


    return redirect('login_registration:success')


# handles existing user login
def login(request):

    if request.method != 'POST':
        return redirect('login_registration:index')

    else:

        # pass form data to User login method to validate valid email and password combination
        # if errors, False is returned,
        #   redirect to login page and show error message
        # else user is in DB and password matches a hashed pw,
        #   store basic user info into session
        #   redirect user to success page and show success message
        user = User.objects.login(request.POST)

        if not user:
            messages.error(request, 'Invalid Login', extra_tags="login")
            return redirect('login_registration:index')

        else:
            request.session['user'] = {
                'id': user[0].id,
                'first_name': user[0].first_name,
                'last_name': user[0].last_name,
                'email': user[0].email
            }
            messages.success(request, 'Successfully logged in!')

    return redirect('login_registration:success')

def logout(request):

    request.session.clear()

    return redirect('login_registration:index')
