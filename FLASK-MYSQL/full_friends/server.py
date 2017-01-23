from flask import Flask, render_template, redirect, request

from mysqlconnection import MySQLConnector

app = Flask(__name__)

mysql = MySQLConnector(app, 'restful_friendsdb')



@app.route('/')
def index():

    # main route renders to index.html which includes a form to add new friend
    # and displays all the friends in DB sorted a-z by last name

    # setup query to select all friends in DB and store it in all_friends
    query = 'SELECT id, UPPER(first_name) AS first_name, UPPER(last_name) AS last_name FROM friends ORDER BY last_name'
    all_friends = mysql.query_db(query)


    return render_template('index.html', all_friends=all_friends)



@app.route('/friends', methods=['POST'])
def create():

    ### handles the add friend form submit, inserts the friend into the DB

    # first run a simple validation on input, check that first and last name are greater than 2 chars
    if not (len(request.form['first_name']) > 2 and len(request.form['last_name']) > 2):

        return redirect('/')

    # get the new friends data from the form
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']
    }

    # set up INSERT query statement
    query = 'INSERT INTO friends (first_name, last_name, created_at) VALUES (:first_name, :last_name, NOW())'

    # add the record
    mysql.query_db(query, data)

    # return to the main page to display all records
    return redirect('/')


@app.route('/friends/<id>/edit', methods=['POST'])
def edit(id):

    ### display the friend data in a form that can be edited by user

    # store id from route for use in query
    data = {
        'id': id
    }

    # set up the query to collect current friend data
    query = 'SELECT id, first_name, last_name FROM friends WHERE id=:id'
    friend_data = mysql.query_db(query, data)

    friend = {
        'id': id,
        'first_name': friend_data[0]['first_name'],
        'last_name': friend_data[0]['last_name']
    }

    # render to edit.html file and show friend data in form so user can edit
    return render_template('edit.html', friend=friend)


@app.route('/friends/<id>', methods=['POST'])
def update(id):

    ### handle the edit friend form submit

    # get all the form data to use for update query
    data = {

        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']

    }

    # create the update query and update DB
    query = 'UPDATE friends SET first_name=:first_name, last_name=:last_name WHERE id=:id'
    mysql.query_db(query, data)

    # return to main page to display all records
    return redirect('/')


# delete friend from DB
@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):

    ### handles the deletion of friend from DB

    # store id from route for use in query
    data = {

        'id': id

    }

    # create the delete query and return to main page to display all current records
    query = 'DELETE FROM friends WHERE id=:id'
    mysql.query_db(query, data)

    return redirect('/')

app.run(debug=True)
