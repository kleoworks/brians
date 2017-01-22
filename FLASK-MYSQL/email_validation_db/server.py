from flask import Flask, render_template, request, redirect, session
from mysqlconnection import MySQLConnector
import re
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'sofmaweorij;jasdfSecret'

# connect to database
mysql = MySQLConnector(app, 'emailsdb')

# set up email validation with regex
email_regex = re.compile(r'[A-Za-z0-9_]+@[A-Za-z0-9]+.[A-Za-z0-9]+')

@app.route('/')
def index():

    if 'message' not in session:
        session['message'] = 'none'

    return render_template('index.html')


# add email to db
@app.route('/add_email', methods=['POST'])
def add_email():

    # store the email grabbed from the form submit for INSERT query and also to show on success page
    data = {
    'email': request.form['email'],
    }

    # check if email is valid, if NOT valid, redirect to index page and show error message
    if not re.match(email_regex, data['email']):
        session['message'] = 'error'
        return redirect('/')

    # update session message and store the email for display back to user upon success
    else:
        session['message'] = 'added_record'
        session['email'] = data['email']

    # set up query to insert new record into db
    # insert the new record
    query = 'INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())'
    mysql.query_db(query, data)

    return redirect('/success')


# show all emails in db
@app.route('/success')
def show():

    # query to select all records in db
    # store query results in all_emails for display back to user
    query = 'SELECT id, email, DATE_FORMAT(created_at, "%m/%d/%y %h:%i%p") AS created_at FROM emails ORDER BY created_at DESC'
    all_emails = mysql.query_db(query)

    # a message will display to user if record was added or deleted through success.html template

    return render_template('success.html', all_emails=all_emails)


# delete email from db
@app.route('/remove_email', methods=['POST'])
def remove_email():

    # get the id that was passed in the forms hidden input
    data = {
        'id': request.form['delete']
    }

    # update session message
    session['message'] = 'deleted_record'

    # set up query to get email that matches id passed through from hidden input before deleting the record # for display upon successful deletion
    get_email_query = 'SELECT email FROM emails WHERE id = :id'
    session['email'] = mysql.query_db(get_email_query, data)[0]['email']

    # delete the email from the db
    delete_query = 'DELETE FROM emails WHERE id = :id'
    mysql.query_db(delete_query, data)

    # show message was successfully deleted and display all remaining emails on success page
    return redirect('/success')

app.run(debug=True)
