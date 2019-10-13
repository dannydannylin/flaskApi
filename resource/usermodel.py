##### import module #####
### python moudle ###
# flask
from flask_restplus import Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
# sqlite
import sqlite3
# json
import json
### my moudle ###
from resource.user import UserDB
from resource.flaskmodule import app, api, db


##### flask decorator #####
@app.route("/ww", methods = ["GET"])
def home():
    return "Flask Restful Api !!!"

##### api decorator #####
@api.route("/print_hello_world", methods = ["GET"])
class PrintHelloWorld(Resource):
    def get(self):
        return {
            'message': 'Hello Wrold!'
        }, 200

@api.route( "/user" )
class UserApi( Resource ):

    # json parameter
    parser = reqparse.RequestParser()
    parser.add_argument('user', required = True, help = 'user is required', location = 'json' )
    parser.add_argument('age', required = True, type = int, help = 'age is required', location = 'json' )

    def __init__( self, Resource ):
        pass

    def get( self ):
        print( "Access get api" )
        return json.loads( str( UserDB.query.all()) ), 200

    def post( self ):
        print( "Access pos api" )
        arg = self.parser.parse_args()
        name = arg['user']
        age = arg['age']
        mydb = UserDB( name, age )
        db.create_all()
        db.session.add( mydb )
        db.session.commit()
        return { "message" : "post success" }, 200

    def put( self ):
        pass

    def delete( self ):
        pass

