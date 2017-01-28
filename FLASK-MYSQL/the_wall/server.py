from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'asdofjompDSlkeiijmekuou'

mysql = MySQLConnector(app, 'walldb')

bcrypt = Bcrypt(app)

email_regex = re.compile(r"[A-Za-z0-9!#$%&'*+-/=?^_`{|}~;]+@[A-Za-z0-9]+.[a-zA-Z]+")


######################
# THE WALL MAIN PAGE #
######################
@app.route('/')
def index():

    # show log-in page if user not already logged in
    if 'user' not in session:
        return render_template('login.html')


    else:

        # run queries to get all messages and comments from DB,
        # store the lists and pass through render_template

        # get messages from DB
        query = 'SELECT messages.id AS id, messages.message AS message, DATE_FORMAT(messages.created_at, "%M %D %Y") AS created_at, CONCAT(users.first_name, " ", users.last_name) AS user, users.id AS user_id, TIME_TO_SEC(TIMEDIFF(CURTIME(), TIME(messages.created_at))) AS time_diff FROM messages LEFT JOIN users ON messages.user_id=users.id ORDER BY messages.created_at DESC'
        messages = mysql.query_db(query)

        # get comments from DB
        query = 'SELECT comments.message_id AS id, comments.comment, DATE_FORMAT(comments.created_at, "%M %D %Y") AS created_at, CONCAT(users.first_name, " ", users.last_name) AS user FROM comments LEFT JOIN users ON comments.user_id=users.id ORDER BY comments.created_at ASC'
        comments= mysql.query_db(query)

        return render_template('index.html', messages=messages, comments=comments)



######################
# POSTS AND COMMENTS #
######################

# adds new message and redirects to wall
@app.route('/messages', methods=['POST'])
def add_message():

    data = {

        'user_id': session['user']['id'],
        'message': request.form['message']

    }

    # basic validation on message, greater than 1 character
    if len(data['message']) <= 1:
        flash('Your message did not seem meaningful enough to post here!')


    # add message to DB and return to wall page to show updated posts
    else:

        # adds the post to DB
        query = 'INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())'
        mysql.query_db(query, data)


    return redirect('/')


# deletes message from wall and any related comments and redirects to wall
@app.route('/messages/<id>/delete')
def delete_message(id):

    data = {
        'id': id
    }

    # delete the messages and any related comments
    messages_query = 'DELETE FROM messages WHERE id=:id'
    comments_query = 'DELETE FROM comments WHERE message_id=:id'

    mysql.query_db(comments_query, data)
    mysql.query_db(messages_query, data)

    return redirect('/')


# adds new message comment and redirects to wall
@app.route('/comments', methods=['POST'])
def add_comment():

    data = {

        'user_id': session['user']['id'],
        'message_id': int(request.form['message_id']),
        'comment': request.form['comment']

    }

    query = 'INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, NOW(), NOW())'
    mysql.query_db(query, data)

    return redirect('/')



##########################################
# LOGIN, LOGOUT, AND REGISTRATION ROUTES #
##########################################

@app.route('/login', methods=['POST'])
def login():

    data = {

        'email': request.form['email'],
        'password': request.form['password']
    }


    # check query returned a record matching an email in DB and verify the password matches for that record
    query = 'SELECT * FROM users WHERE email LIKE :email'
    user = mysql.query_db(query, data)

    # query returned no result, or password is less than 8 characters (not valid), or password does not match password in DB
    if not user or len(data['password']) < 8 or not bcrypt.check_password_hash(user[0]['password'], data['password']):

        flash('Please enter a valid email and password')

    else:

        # log in was successful, allow user to see wall page and add user to session
        session['user'] = {

            'id': user[0]['id'],
            'first_name': user[0]['first_name'],
            'last_name': user[0]['last_name'],
            'email': user[0]['email'],

        }

    return redirect('/')


@app.route('/register')
def show_form():

    # if user already logged in and found their way to this page, redirect them to the wall page
    if 'user' in session:
        return redirect('/')

    else:

        # show registration form to user
        return render_template('register.html')


@app.route('/users', methods=['POST'])
def add_user():

    # error flag for flash messaging if any form data does not validate
    # if stays false during validation, go ahead and add user to DB
    # if turns true, redirect user to registration page and show error messages
    error = False

    data = {

        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirm_password': request.form['confirm_password']

    }

    # validate first and last name
    if data['first_name'] == "" or len(data['first_name']) < 2:
        flash('First name can not be blank or less than 2 characters')
        error = True

    if data['last_name'] == "" or len(data['last_name']) < 2:
        flash('Last name can not be blank or less than 2 characters')
        error = True

    # validate email
    # not in DB, not empty, is valid email format
    query = 'SELECT * FROM users WHERE email LIKE :email'
    query_email = mysql.query_db(query, data)
    if query_email or data['email'] == "" or not re.match(email_regex, data['email']):
        flash('Please re-enter a valid email or login if you already are registered')
        error = True

    # validate passwords
    # at least 8 characters, matches confirm password
    if len(data['password']) < 8 or data['password'] != data['confirm_password']:
        flash('Please make sure your password is at least 8 characters')
        error = True


    # validations didn't pass, return to registration page and show errors
    if error == True:
        return redirect('/register')

    # validations passed, generate pw hash and add user to DB, then redirect to login page and show successfully registered message
    else:

        data['pw_hash'] = bcrypt.generate_password_hash(data['password'])

        query = 'INSERT INTO users SET first_name=:first_name, last_name=:last_name, email=:email, password=:pw_hash, created_at=NOW(), updated_at=NOW()'
        mysql.query_db(query, data)

        flash('Successfully registered, please login')
        return redirect('/')


@app.route('/logout')
def logout():

    #handles user logout
    #delete user from session
    #redirect to login page
    del session['user']
    return redirect('/')

app.run(debug=True)
