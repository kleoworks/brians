from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

# create a class that will give us an object that we can use to connect a database
class MySQLConnection(object):
    def __init__(self, app, db):
        config = {
            'host': 'localhost',
            'database': db,
            'user': 'root',
            'password': 'root',
            'port': '3306' # must match port your SQL server is running on
        }

        DATABASE_URI = "mysql://{}:{}@127.0.0.1:{}/{}".format(config['user'], config['password'], config['port'], config['database'])

        app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

        # establish the connection to the database
        self.db = SQLAlchemy(app)

    # method used to query database
    def query_db(self, query, data=None):
        result = self.db.session.execute(text(query),data)

        # if the query was a select
        if query[0:6].lower() == 'select':

            # convert the result to list fo dicts
            list_result = [dict(r) for r in result]
            return list_result

        # if the query was an insert
        elif query[0:6].lower() == 'insert':

            # return the id of the commit changes
            self.db.session.commit()
            return result.lastrowid

        # else the query was an update or delete, return nothing and just commit the changes
        else:
            self.db.session.commit()

# method to be called by the user in server.py
def MySQLConnector(app, db):
    return MySQLConnection(app,db)
