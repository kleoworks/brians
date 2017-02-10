from __future__ import unicode_literals

from django.db import models

from datetime import datetime

import re

import bcrypt

regex_alpha = re.compile(r'[A-Za-z]+')
regex_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
regex_date = re.compile(r'\d{1,2}\/\d{1,2}\/\d{4}')

class UserManager(models.Manager):

    def register(self, data):

        # add user to DB after validating all user inputs
        User.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=data['password'], birthday=data['birthday'])
        user = User.objects.filter(email=data['email'])
        return user


    def login(self, postData):

        # if email or password is empty, or email is not found in DB return False, do not login
        if postData['email'] == "" or postData['password'] == "" or not User.objects.filter(email=postData['email']):
            return False

        # store user object from DB
        user = User.objects.filter(email=postData['email'])

        # if the password submitted does not match the hashed PW in DB return False, do not login
        if not bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()) == user[0].password.encode():
            return False

        else:
            # the email is in DB and the password matches, login user
            return user


    # handles hashing the password if we are registering a new user
    def hash_pw(self, password):

        # hash pw
        return bcrypt.hashpw(password, bcrypt.gensalt())


    def validate_new_user(self, postData):

        # create empty list to store any error messages when validating user inputs
        # if any error messages after validations, return errors, do not register user
        # if no errors, go ahead and add user to DB
        error_messages = []

        if len(postData['first_name']) < 2:
            error_messages.append('First name required')
        elif not re.match(regex_alpha, postData['first_name']):
            error_messages.append('First name must contain letters only')

        if len(postData['last_name']) < 2:
            error_messages.append('Last name required')
        elif not re.match(regex_alpha, postData['last_name']):
            error_messages.append('Last name must contain letters only')

        if postData['email'] == "":
            error_messages.append('Email address required')

        elif not re.match(regex_email, postData['email']):
            error_messages.append('Email address not a valid format')

        elif User.objects.filter(email=postData['email']):
            error_messages.append('That email address is already in use.')

        if len(postData['password']) < 8 or postData['password'] == '':
            error_messages.append('Password must be at least 8 characters')
        elif postData['password'] != postData['confirm_pw']:
            error_messages.append('Password must match password confirmation')

        if not re.match(regex_date, postData['birthday']):
            error_messages.append('Please enter a valid birthday in mm/dd/yyyy format')

        else:

            try:
                birthday = datetime.strptime(postData['birthday'], '%m/%d/%Y')
                today = datetime.now()
                today = datetime.replace(today, hour=0, minute=0, second=0, microsecond=0)
                if birthday >= today:
                    error_messages.append('Your birthday can not be on or after today!')

            except ValueError:
                error_messages.append('Please enter a valid birthday')

        if error_messages:

            return ("error", error_messages)

        else:

            # validations succeeded

            # create pw hash
            password = self.hash_pw(postData['password'].encode())

            # package the form data with pw hash and birthday as datetime object for inserting into DB
            data = {

                'first_name': postData['first_name'],
                'last_name': postData['last_name'],
                'email': postData['email'],
                'password': password,
                'birthday': birthday

            }

            # add user to DB
            user = self.register(data)

            # return newly created user
            return user



class User(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.DateField()
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
