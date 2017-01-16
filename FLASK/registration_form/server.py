from flask import Flask, render_template, redirect, request, session, flash
import re
from datetime import datetime, date

app = Flask(__name__)

app.secret_key = 'l;kasdf;ljSecret;kasdf;oijKey;lasdf;l'
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
pwd_regex = re.compile(r'^(?=[^A-Z]*[A-Z])(?=[^0-9]*[0-9])[\w\d]{8,}$')
date_regex = re.compile(r'([0-1][0-9])\/([0-3][0-9])\/([1-9][0-9][0-9][0-9])')

@app.route('/')
def index():

    return redirect('/form')

@app.route('/form')
def register():

    return render_template('register.html')

@app.route('/process', methods=['POST'])
def validate():

    # check if email is blank
    if len(request.form['email']) < 1:
        flash("Email can't be blank", 'blank')

    # check if email is valid
    elif not email_regex.match(request.form['email']):
        flash("'{}' is not a valid email address".format(request.form['email']), 'invalid')

    else:
        email = request.form['email']


    # check that first name not blank, and only includes alpha characters
    if len(request.form['first_name']) < 1:
        flash("First name can't be blank", 'blank')

    elif not request.form['first_name'].isalpha():
        flash("Enter a valid first name", 'invalid')

    else:
        first_name = request.form['first_name']


    # check that last name not blank, and only includes alpha characters
    if len(request.form['last_name']) < 1:
        flash("Last name can't be blank", 'blank')

    elif not request.form['last_name'].isalpha():
        flash('Enter a valid last name', 'invalid')

    else:
        last_name = request.form['last_name']


    # validate password longer
    # must be longer than 8 characters
    # and have at least 1 uppercase letter and 1 number

    password = request.form['password']

    if len(password) < 1:
        flash("Password can't be blank", 'blank')

    elif not pwd_regex.match(password):
        flash('Passwords must be 8 characters or longer and include at least 1 upper case letter and 1 number', 'invalid')

    # confirm passwords match
    elif password != request.form['confirm_password']:
        print password
        print request.form['confirm_password']
        flash("Passwords entered do not match", 'invalid')


    # check that birth date is a valid date and from the past
    # use regex to create match object with 3 groups (month, day, year) to set up date for comparision to todays date
    birth_date_valid = date_regex.match(request.form['birth_date'])
    today = date.today()

    # was birth date blank?
    if len(request.form['birth_date']) < 1:
        flash("Birth date can't be blank", 'blank')

    else:

        # did user enter birth date according to format instructions?  "MM/DD/YYYY"
        if not birth_date_valid: #is checking if matched regex object
            flash('Please enter your birthdate in the format: MM/DD/YYYY', 'invalid')

        # check that the users birthday is before today's date
        else:
            # first convert users birthday to date object to compare if valid date
            birth_date = date(int(birth_date_valid.group(3)), int(birth_date_valid.group(1)), int(birth_date_valid.group(1)))

            if not birth_date < today:
                flash("This isn't back to the future!  Enter a valid date.", 'invalid')


    return redirect('/')

app.run(debug=True)
