from flask_restful import Resource, reqparse
import sqlite3

from db.db import db


class User():

    __tablename__ = 'users'
    name = db.Column(db.String(80), unique=True, nullable=False)

    user = []
    userdict = {}

    parser = reqparse.RequestParser()
    parser.add_argument('user', required = True, help = 'user is required', location = 'json' )
    
    def __init__( self ):
        pass

    def get(self, name):

        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        query_one_query = 'SELECT * FROM users'
        i = 1
        for item in cursor.execute(query_one_query):
            count = "user" + str( i )
            self.userdict[count] = item
            i += 1

        if i == 1:
            return { "message" : "No user" }

        return self.userdict

    def post(self, name):
        arg = self.parser.parse_args()
        val = "\"" + arg['user'] + "\""
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        insert_query = 'INSERT INTO users ( name ) VALUES ( %s )' %( val )
        cursor.execute( insert_query )
        conn.commit()
        conn.close()
        
        return {
            'message': 'Insert user success'
        }


    def put(self, name):
        pass

    def delete(self, name):
        del self.user[:]
        self.userdict.clear()
        return { "message" : "Delete Done" }