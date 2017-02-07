from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Email

import re
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



def index(request):

    return render(request, 'email_validation/index.html')



def success(request):

    context = {

        'emails': Email.objects.all().order_by('-created_at')

    }

    return render(request, 'email_validation/results.html', context)


# handles email validation and adding email record to DB
def process(request):

    # if made it to this page other than POST, redirect to main page
    if request.method != 'POST':

        return redirect('/')

    # if email is not a valid email, redirect to main page and show error message
    if not re.match(email_regex, request.POST['email']):

        messages.error(request, 'Email is not valid!')
        return redirect('/')

    # email is valid, add email to DB, redirect user to success page and show success message
    else:

        email = Email.objects.create(email=request.POST['email'])
        messages.success(request, 'The email address you entered %s is a VALID email address!  Thank you!' % email.email)
        return redirect('/success')


# handles deleting an email from DB
def destroy(request, id):

    # get email by ID, passed through a tag/link
    # delete the email from DB, redirect to success page and show success message
    email = Email.objects.get(id=id)
    email.delete()
    messages.success(request, 'The email address %s was successfully deleted' % email.email)
    return redirect('/success')
