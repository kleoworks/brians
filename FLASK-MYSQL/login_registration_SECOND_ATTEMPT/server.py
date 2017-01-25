from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)

bcrypt = Bcrypt(app)

mysql = MySQLConnector(app, 'usersdb')

app.secret_key = 'asdomekSecretKeysdflasd'

email_regex = re.compile(r'[A-Za-z0-9_]+@[A-Za-z]+.[a-zA-Z]+')

@app.route('/')
def index():

    ## show login page if user not logged in OR show index.html if user already logged in
    # the user information is captured during login and stored in session if login was successful

    # user not logged in, show login page
    if 'user' not in session:
        return render_template('login.html')

    # user logged in, show index.html
    else:
        return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():

    # get form data, convert non-password fields to uppercase for comparison to records in DB
    data = {

        'email': request.form['email'].upper(),
        'password': request.form['password']
    }

    # do simple validation on login input and if email exists in DB, if errors show flash message to user an reload login page
    # else if no errors and passwords match, allow user to login, set session['user'] with all query data, and redirect to index.html
    query = 'SELECT * FROM users WHERE email LIKE :email'
    user = mysql.query_db(query, data)

    if not user or len(data['password']) < 8 or not bcrypt.check_password_hash(user[0]['pw_hash'], data['password']):
        flash('Please enter a valid username and password')
        return redirect('/')

    else:

        session['user'] = {

            'id': user[0]['id'],
            'first_name': user[0]['first_name'],
            'last_name': user[0]['last_name'],
            'email': user[0]['email']
        }

        return redirect('/')



@app.route('/register')
def show_registration():

    ## show the registration form

    return render_template('register.html')


@app.route('/users', methods=['POST'])
def add_user():

    # set an error flag for use when redirecting user upon validation of form
    # if error stays False, user will get inserted into DB
    # if error turns True, return user to registrationform and show flash error messages
    error = False

    # get form data, convert non-password fields to uppercase for comparison to records in DB
    data = {
        'first_name': request.form['first_name'].upper(),
        'last_name': request.form['last_name'].upper(),
        'email': request.form['email'].upper(),
        'password': request.form['password'],
        'confirm_password': request.form['confirm_password']
    }

    ## do basic validations, and set error flag to True if any validations fail

    # first name and last name validations
    if data['first_name'] == "":
        flash('FIRST NAME CAN NOT BE BLANK')
        error = True

    elif len(data['first_name']) < 2:
        flash('FIRST NAME SHOULD BE GREATER THAN 2 CHARACTERS')
        error = True

    if data['last_name'] == "":
        flash('LAST NAME CAN NOT BE BLANK')
        error = True

    elif len(data['last_name']) < 2:
        flash('LAST NAME SHOULD BE GREATER THAN 2 CHARACTERS')
        error = True

    # email validations
    # MUST query to see if email already exists in DB!!!!!  Or you will have serious issues later!!!
    email_query = 'SELECT * FROM users WHERE email LIKE :email'
    duplicate_email = mysql.query_db(email_query, data)

    if data['email'] == "":
        flash('EMAIL CAN NOT BE BLANK')
        error = True

    elif not re.match(email_regex, data['email']):
        flash('PLEASE ENTER A VALID EMAIL')
        error = True

    elif duplicate_email:
        flash('EMAIL ALREADY IN USE')
        error = True

    # password validations
    if data['password'] == "":
        flash('PASSWORD CAN NOT BE BLANK')
        error = True

    elif len(data['password']) < 8:
        flash('PASSWORD SHOULD BE GREATER THAN 8 CHARACTERS')
        error = True

    if data['confirm_password'] == "":
        flash('CONFIRM PASSWORD CAN NOT BE BLANK')
        error = True

    elif data['confirm_password'] != data['password']:
        flash('PASSWORDS DO NOT MATCH')
        error = True

    # if error flag is true, redirect to registration page and show errors
    if error == True:
        return redirect('/register')


    # no validation errors found, we can add user to DB
    else:
        # generate pw hash, add user to DB and redirect to login page
        data['pw_hash'] = bcrypt.generate_password_hash(data['password'])

        query = 'INSERT INTO users SET first_name=:first_name, last_name=:last_name, email=:email, pw_hash=:pw_hash, created_at=NOW(), updated_at=NOW()'
        mysql.query_db(query, data)

        return redirect('/')


@app.route('/logout', methods=['POST'])
def logout():

    # handle user logout
    # delete user from session dict, redirect to login page
    del session['user']
    return redirect('/')

app.run(debug=True)
