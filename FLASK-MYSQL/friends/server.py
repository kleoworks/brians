from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector


app = Flask(__name__)

mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def index():

    friends = mysql.query_db('SELECT * FROM friends')
    print friends
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():

    return redirect('/')

@app.route('/friends/<friend_id>')
def show(friend_id):

    query = 'SELECT * FROM friends WHERE id = :specific_id'

    data = {
        'specific_id': friend_id
    }

    friends = mysql.query_db(query, data)

    return render_template('index.html', one_friend=friends[0])

app.run(debug=True)
