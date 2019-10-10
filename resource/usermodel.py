from flask_restful import Resource
import sqlite3

from resource.user import User

class UserModel( Resource ):

    myuser = User()

    def __init__( self ):
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users('
                    'name VARCHAR(20) PRIMARY KEY)'
                    )

        conn.commit()
        conn.close()

    def get( self, name ):
        return self.myuser.get( name ), 200

    def post( self, name ):
        return self.myuser.post( name ), 200

    def put( self, name ):
        pass

    def delete( self, name ):
        return self.myuser.delete( name ), 200