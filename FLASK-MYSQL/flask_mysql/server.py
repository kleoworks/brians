from flask import Flask

# import the connector function from mysqlconnetion.py
from mysqlconnection import MySQLConnector

app = Flask(__name__)

# connect and store the connection and pass in the database NAME you are connecting to
mysql = MySQLConnector(app, 'mydb')

print mysql.query_db("SELECT * FROM users")

app.run(debug=True)
