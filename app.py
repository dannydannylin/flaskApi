from flask import Flask
from flask_restful import Api, Resource
import sqlite3
from flask_sqlalchemy import SQLAlchemy

from resource.user import User
from resource.usermodel import UserModel



app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:/tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/", methods = ["GET"])
def home():
    return "Flask Restful Api !!!"


class PrintHelloWorld(Resource):
    def get(self):
        return {
            'message': 'Hello Wrold!'
        }, 200

api.add_resource(PrintHelloWorld, "/print_hello_world")
api.add_resource(UserModel, "/user/<string:name>")

if __name__ == "__main__":
    
    app.run()