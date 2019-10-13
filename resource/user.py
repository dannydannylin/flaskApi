
import sqlite3

from resource.flaskmodule import db

class UserDB( db.Model ):
    # table name
    __tablename__ = 'users'
    # column ( attribute )
    id = db.Column( db.Integer, primary_key = True )
    username = db.Column( db.String( 80 ), unique = False, nullable = True )
    age = db.Column( db.Integer, nullable = True )

    def __init__( self, username, age ):
        self.username = username
        self.age = age
        
    def __repr__( self ):
        return '{\"%s\" : \"%d\"}' % ( self.username, self.age )
