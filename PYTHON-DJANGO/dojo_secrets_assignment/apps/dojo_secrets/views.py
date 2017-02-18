from django.shortcuts import render, redirect
from django.db.models import Count
from django.contrib import messages
from .models import Secret
from ..login_registration.models import User

def index(request):

    # THIS VIEW SHOWS 5 MOST RECENT SECRETS ONLY ##
    # check if user in session, if not then return to login page
    # else get user instance from DB for use in related queries,
    #   using context, query 4 sets of data for display in template
    #   1. all secrets with count of num_likes
    #   2. secrets created by current user
    #   3. secrets liked by current user
    #   4. all other secrets (not created by user or liked by user)
    #   HTML template will loop over (1) all secrets, and give different functionality to user depending on the query sets 2 - 4

    if 'user' not in request.session:
        return redirect('login_registration:index')

    else:

        user = User.objects.get(id=request.session['user']['id'])

        context = {
            'all_secrets': Secret.objects.all().annotate(num_likes=Count('likes')).order_by('-created_at')[:5],
            'user_secrets': Secret.objects.filter(user=user),
            'liked_secrets': Secret.objects.filter(likes=user),
            'other_secrets': Secret.objects.all().exclude(user=user).exclude(likes=user)
        }

        return render(request, 'dojo_secrets/index.html', context)


def popular(request):

    # THIS VIEW SHOWS ALL SECRETS RANKED FROM MOST LIKED AND RECENT ##
    # THE QUERIES USED IN THIS VIEW FOLLOW THE SAME FORMAT AS THOSE IN MAIN INDEX
    # check if user in session, if not then return to login page
    # else get user instance from DB for use in related queries,
    #   using context, query 4 sets of data for display in template
    #   1. all secrets with count of num_likes
    #   2. secrets created by current user
    #   3. secrets liked by current user
    #   4. all other secrets (not created by user or liked by user)
    #   HTML template will loop over (1) all secrets, and give different functionality to user depending on the query sets 2 - 4

    if 'user' not in request.session:
        return redirect('login_registration:index')

    else:

        user = User.objects.get(id=request.session['user']['id'])

        context = {

            'all_secrets': Secret.objects.all().annotate(num_likes=Count('likes')).order_by('-num_likes', 'created_at'),

            'user_secrets': Secret.objects.filter(user=user),

            'liked_secrets': Secret.objects.filter(likes=user),

            'other_secrets': Secret.objects.exclude(user=user).exclude(likes=user)

        }

        return render(request, 'dojo_secrets/popular.html', context)


def create(request):

    # CREATE A SECRET
    #  Do basic validation, if empty return error to user
    #  else add secret to DB and redirect to main index page
    if request.POST['secret'] == "":
        messages.error(request, 'Really?? No secret worth sharing??')

    else:
        user = User.objects.get(id=request.session['user']['id'])
        my_secret = Secret.objects.create(content=request.POST['secret'], user=user)

    return redirect('dojo_secrets:index')


def like(request, secret_id):

    # LIKE A SECRET
    #  Get user instance from DB, get secret instance from DB, and add the user instance to the likes mtm field
    # redirect to main index page
    user = User.objects.get(id=request.session['user']['id'])
    secret = Secret.objects.get(id=secret_id)
    secret.likes.add(user)

    return redirect('dojo_secrets:index')


def destroy(request, secret_id):

    # DELETE A SECRET
    # Only allow deletion of secret if the current user is the creator of the secret
    get_secret = Secret.objects.get(id=secret_id)

    if request.session['user']['id'] == get_secret.user.id:

        Secret.objects.get(id=secret_id).delete()

    return redirect(request.META['HTTP_REFERER'])
