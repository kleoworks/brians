from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Description

def index(request):

    # get courses and descriptions
    context = {

        'courses': Course.objects.all(),
        'description': Description.objects.all()

    }

    return render(request, 'courses/index.html', context)


def create(request):

    # do basic validation on form name
    if len(request.POST['name']) < 2:
        messages.error(request, 'Enter valid course name')
        return redirect('/')

    context = {

        'name': request.POST['name'],
        'description': request.POST['description'] # we are going to add description even if empty

    }

    # create new course
    course = Course.objects.create(name=context['name'])

    # add the course's description, using the newly created course's ID
    Description.objects.create(description=context['description'], course=course)

    return redirect('/')



def destroy(request, id):

    # show the course name and description to user and confirm deletion
    # NO button will redirect to main course page
    # YES button will delete the course record from DB and redirect to main course page
    if request.method == 'GET':

        context = {

            'id': id,
            'course': Course.objects.get(id=id)

        }

        return render(request, 'courses/confirm_delete.html', context)

    else:

        Course.objects.get(id=id).delete()
        return redirect('/')
