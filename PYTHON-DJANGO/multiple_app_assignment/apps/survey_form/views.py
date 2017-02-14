from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):

    # show survey form to user
    return render(request, 'survey_form/index.html')


def result(request):

    # show survey results to user
    return render(request, 'survey_form/result.html')


def process_survey(request):

    # if you made it to this route with a POST request
    # do basic validation on name field, if blank return to survey and show error message
    # otherwise process survey form, adding all values to session and incrementing count each time form submitted

    if request.method == 'POST':

        if request.POST['name'] == "":
            messages.error(request, "Name field can not be blank")
            return redirect ('survey_form:index')

        else:

            request.session['name'] = request.POST['name']
            request.session['location'] = request.POST['location']
            request.session['language'] = request.POST['language']
            request.session['comment'] = request.POST['comment']

        if 'count' not in request.session:
            request.session['count'] = 1
        else:
            request.session['count'] += 1

        return redirect('survey_form:result')

    # else redirect to index.html and show survey form
    else:

        return redirect('survey_form:index')
