from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'semi_restful_usersdb')

app.secret_key = 'asfl;kjasd;keijSecret'

email_regex = re.compile(r"[A-Za-z0-9!#$%&'*+-/=?^_`{|}~;]+@[A-Za-z0-9]+.[a-zA-Z]+")

@app.route('/')
def index():

    session['last_page'] = '/'

    #default route, show all users
    query = 'SELECT id, CONCAT(first_name, " ", last_name) AS full_name, email, DATE_FORMAT(created_at, "%M %D, %Y") AS created_at FROM users ORDER BY id'
    users = mysql.query_db(query)

    return render_template('index.html', users=users)

@app.route('/users/new')
def new_user():

    # show new user form
    return render_template('new.html')


@app.route('/users/create', methods=['POST'])
def add_user():

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    # basic validations: form fields not empty, and email valid email
    if data['first_name'] == "" or data['last_name'] == "" or data['email'] == "" or not re.match(email_regex, data['email']):
        flash('Please enter valid information in all fields')

        # validations didn't pass, redirect to new user page and show error
        return redirect('/users/new')


    # form data validated, okay to add user to DB then redirect to main page to show all users
    query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())'
    mysql.query_db(query, data)

    return redirect('/')


@app.route('/users/<id>')
def show_user(id):

    session['last_page'] = '/users/{}'.format(id)

    data = {
        'id': id
    }

    # get user info from DB from user ID passed through URL and show user information
    query = 'SELECT id, CONCAT(first_name, " ", last_name) AS full_name, email, DATE_FORMAT(created_at, "%M %D %Y") AS created_at FROM users WHERE id=:id'
    user = mysql.query_db(query, data)

    return render_template('show.html', user=user)

@app.route('/users/<id>/edit')
def edit_user(id):

    data = {
        'id': id
    }

    #populate form inputs with current user info from DB
    query = 'SELECT id, first_name, last_name, email FROM users WHERE id=:id'
    user = mysql.query_db(query, data)

    return render_template('edit.html', user=user[0])


@app.route('/users/<id>', methods=['POST'])
def update_user(id):

    data = {
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    # basic validations: form fields not empty, and email valid email
    if data['first_name'] == "" or data['last_name'] == "" or data['email'] == "" or not re.match(email_regex, data['email']):
        flash('Please try again and make sure no fields are blank and you are using a valid email address')

        # validations didn't pass, redirect to new user page and show error
        return redirect('/users/{}/edit'.format(id))

    # form data validated, okay to update user info in DB then redirect to main page to show all users
    query = 'UPDATE users SET first_name=:first_name, last_name=:last_name, email=:email, updated_at=NOW() WHERE id=:id'
    mysql.query_db(query,data)

    return redirect('/')

@app.route('/users/<id>/destroy')
def delete_user(id):

    data = {
        'id': id
    }

    query = 'DELETE FROM users WHERE id=:id'
    mysql.query_db(query, data)

    return redirect('/')


app.run(debug=True)
