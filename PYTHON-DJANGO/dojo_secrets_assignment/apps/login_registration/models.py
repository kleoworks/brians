from __future__ import unicode_literals

from django.db import models

import re
import bcrypt

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def validate_login(self, postData):

        messages = []

        if postData['email'] == "" or not re.match(email_regex, postData['email']) or postData['password'] == "" or len(postData['password']) < 8 or not User.objects.filter(email=postData['email']):
            messages.append('Invalid login')
            return (False, messages)


        get_user = User.objects.filter(email=postData['email'])
        hashed_pw = get_user[0].password.encode()

        if not bcrypt.hashpw(postData['password'].encode(), hashed_pw) == hashed_pw:
            messages.append('Invalid login')
            return (False, messages)

        else:

            user = {

                'id': get_user[0].id,
                'first_name': get_user[0].first_name
            }

            return (True, user)


    def validate_new_user(self, postData):

        messages = []

        if postData['first_name'] == "":
            messages.append('First name cannot be blank')
        elif len(postData['first_name']) < 2:
            messages.append('Please enter a valid first name')

        if postData['last_name'] == "":
            messages.append('Last name cannot be blank')
        elif len(postData['last_name']) < 2:
            messages.append('Please enter a valid last name')

        if postData['email'] == "":
            messages.append('Email cannot be blank')

        elif not re.match(email_regex, postData['email']):
            messages.append('Please enter a valid email')

        elif User.objects.filter(email=postData['email']):
            messages.append('That email already in use')

        if postData['password'] == "":
            messages.append('Password cannot be blank and must be at least 8 characters long')
        elif len(postData['password']) < 8:
            messages.append('Password must be at least 8 characters long')
        elif postData['password'] != postData['confirm_password']:
            messages.append('Password must match confirm password')


        if len(messages) > 0:
            return (False, messages)
        else:
            response = self.add_user(postData)
            return response


    def add_user(self, postData):

        pw_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())

        new_user = User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=pw_hash)

        user = {

            'id': new_user.id,
            'first_name': new_user.first_name
        }

        return (True, user)


class User(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):

        return self.first_name + " " + self.last_name
