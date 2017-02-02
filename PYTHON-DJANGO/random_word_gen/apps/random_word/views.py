from django.shortcuts import render, redirect
import random

def index(request):

    # we don't want to show a new attempt upon page refresh, only when generating a new random word
    # if random_word is not in session, redirect to get_random route to make one
    # else a session has started, so let's show your new random word and count on the page

    if 'random_word' not in request.session:
        return redirect('/get_random')

    else:
        return render(request, 'random_word/index.html')

def get_random(request):

    # session.count and session.random_word will hold our values

    # start counting number of times we have generated a random word
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    # create an empty string to hold the random word
    # use randint on the chars string 14 times to create the new word
    # redirect to index page to show random word and count
    word = ""
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

    for i in range(14):
        word += chars[random.randint(0,len(chars)-1)]

    request.session['random_word'] = word

    return redirect('/')
