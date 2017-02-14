from __future__ import unicode_literals

from django.db import models
from django.db.models import Count
from ..login_registration.models import User
from django.contrib import messages


class CourseManager(models.Manager):

    def enroll_user(self, postData):

        # validate option input, if passed empty "" value for either course or user, return false, and show error message
        if not postData['course'] or not postData['user']:

            return ('Empty', 'Please select a valid user and course')

        # add the user to the course
        else:
            course_id = int(postData['course'])
            user_id = int(postData['user'])

            user = User.objects.get(id=user_id)
            course = Course.objects.get(id=course_id)

            # check if user already in course
            # if already in course, return False and message
            # else add to course, return True and message
            users = course.users.filter(id=user_id)

            if users:
                print '*'*50
                print users
                print '*'*50
                return (False, {'user': user.first_name, 'course': course.name })
            else:
                course.users.add(user)

        # return success message
        return (True, {'user': user.first_name, 'course': course.name })


class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name="courses")
    objects = CourseManager()

    def __str__(self):
        return self.name

class Description(models.Model):
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.OneToOneField(Course)


    def __str__(self):
        return self.name
