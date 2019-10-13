from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api
import os

##### setting #####
# set flask and SQLAlchemy
# get absolute path in working space
pjdir = os.path.abspath( os.path.dirname( __file__ ) )
# get and set flask module
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(pjdir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# restful api
api = Api(app)
# SQLAlchemy
db = SQLAlchemy(app)

# @app.route("/wow", methods = ["GET"])
# def home2():
#     return "wow wow wow !!!"