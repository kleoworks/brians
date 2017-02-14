from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import Course, Description
from ..login_registration.models import User

def index(request):

    if 'user' not in request.session:

        return redirect('login_registration:index')

    # get courses and descriptions
    context = {

        'courses': Course.objects.all().order_by('name'),
        'description': Description.objects.all()

    }

    return render(request, 'courses/index.html', context)


def create(request):

    # do basic validation on form name
    if len(request.POST['name']) < 2:
        messages.error(request, 'Enter valid course name')
        return redirect('courses:index')

    context = {

        'name': request.POST['name'],
        'description': request.POST['description'] # we are going to add description even if empty

    }

    # create new course
    course = Course.objects.create(name=context['name'])

    # add the course's description, using the newly created course's ID
    Description.objects.create(description=context['description'], course=course)

    return redirect('courses:index')



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
        return redirect('courses:index')


def users_courses(request):

    if request.method == 'POST':

        # query DB to enroll User into Course
        response = Course.objects.enroll_user(request.POST)

        # check response from query, if Empty or False return error messages
        # if True, show success message,
        if response[0] == 'Empty':
            messages.error(request, response[1])

        elif response[0] == False:
            messages.error(request, '{} is already enrolled in {}'.format(response[1]['user'], response[1]['course']))

        else:
            messages.success(request, '{} was successfully added to {}'.format(response[1]['user'], response[1]['course']))

    # query DB to get all course info and number of users currently enrolled in each course
    context = {
        'users': User.objects.all().order_by('first_name', 'last_name'),
        'courses': Course.objects.annotate(num_users=Count('users')).order_by('name')
    }


    return render(request, 'courses/users_courses.html', context)
