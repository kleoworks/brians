from flask import Flask, render_template, redirect, request, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key = 'asdf;lkjpasdipjvkljkla333sfqewckeysesdcret'

mysql = MySQLConnector(app, 'usersdb')

email_regex = re.compile(r'[A-Za-z0-9_]+@[A-Za-z0-9]+.[A-Za-z]+')


@app.route('/')
def login():

    ## show main login page and any login error messages if they exist from prior attempts

    # did user just register or try to register with problems???
    # delete registration messages if they exist in current session
    if 'register_msg' in session:
        del session['register_msg']

    # if user already logged in, render index.html instead of login page
    if 'id' in session:
        return render_template('index.html')


    return render_template('login.html')


@app.route('/login', methods=['POST'])
def verify_user():

    ## validate login information
    ## redirect user to login page to retry if login info not valid

    # clear any past log-in messages if they exist, and set up new empty string to track log-in errors
    if 'login_msg' in session:
        del session['login_msg']

    # get data from form submit
    data = {
        'email': request.form['email'],
        'password': request.form['password']
    }

    # check if email is in valid format, no fields are empty, and that password is not less than 8 chars
    # set login error message if any errors
    if not re.match(email_regex, data['email']) or data['email'] == "" or data['password'] == "" or len(data['password']) < 8:
        session['login_msg'] = ['Please enter a valid email and password to login']

        # if any errors redirect to login page and show errors
        return redirect('/')


    # if inputs seem valid, now verify if email and password match a record in DB
    # set up query
    query = 'SELECT * FROM users WHERE email=:email'
    login_query = mysql.query_db(query, data)

    if login_query:

        if bcrypt.check_password_hash(login_query[0]['pw_hash'], data['password']):
            # if passwords match
            # set session user so user no longer needs to log-in
            # show index.html page
            session['id'] = login_query[0]['id']
            session['first_name'] = login_query[0]['first_name']
            session['last_name'] = login_query[0]['last_name']
            return redirect('/')


    # no matching result found, could mean email or password is incorrect, or email not even in DB... hmmm...
    # return user to log-in page with vague error message
    session['login_msg'] = ['Please try again with a valid username and password']

    return redirect('/')


@app.route('/register')
def register():

    ## show registration page
    # if user already logged in, don't let them register!!!
    if 'id' in session:
        return redirect('/')

    return render_template('registration.html')



@app.route('/users', methods=['POST'])
def add_user():

    ## handle registration form validation and addition of user to DB if valid
    ## if any information not valid, redirect to registration page and show error messages

    # clear any past registration attempt messages if they exist, and set up new list to track any validation errors
    if 'register_msg' in session:
        del session['register_msg']

    session['register_msg'] = []


    # get data from form submit
    data = {

        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirm_password': request.form['confirm_password']

    }

    # set up query to check if email already exists in DB
    query = 'SELECT email FROM users WHERE email LIKE :email'
    email_query = mysql.query_db(query, data)

    # validate first_name not empty or < 2 chars
    if data['first_name'] == "":
        session['register_msg'].append('First name can not be blank')

    elif len(data['first_name']) < 2:
        session['register_msg'].append('First name can not be less than 2 characters')

    # validate last_name not empty or < 2 chars
    if data['last_name'] == "":
        session['register_msg'].append('Last name can not be blank')

    elif len(data['last_name']) < 2:
        session['register_msg'].append('Last name can not be less than 2 characters')

    # validate email not empty and valid email
    if data['email'] == "":
        session['register_msg'].append('Email can not be blank')

    elif not re.match(email_regex, data['email']):
        session['register_msg'].append('Email not a valid email')

    # validate password is not empty or < 8 characters
    if data['password'] == "":
        session['register_msg'].append('Password can not be blank')

    elif len(data['password']) < 8:
        session['register_msg'].append('Password must be at least 8 characters')

    # validate confirm password in not empty or < 8 and matches password
    if data['confirm_password'] == "":
        session['register_msg'].append('Confirm password can not be blank')

    elif len(data['confirm_password']) < 8:
        session['register_msg'].append('Confirm password did not match')

    elif data['password'] != data['confirm_password']:
        session['register_msg'].append('Passwords do not match')

    # check if email already exists in database
    if email_query:

        if data['email'] == email_query[0]['email']:
            session['register_msg'].append('That email already exists!')

    # if any registration error messages, then return user to registration form and show errors
    if len(session['register_msg']) > 0:
        return redirect('/register')

    # no errors found so we can add user to DB and return to login page to log-in
    # first encrypt the password
    pw_hash = bcrypt.generate_password_hash(data['password'])
    data['password'] = pw_hash

    query = 'INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())'
    mysql.query_db(query, data)

    # go to login page
    return redirect('/')

app.run(debug=True)
