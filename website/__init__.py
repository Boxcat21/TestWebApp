# NOTES ABOUT FILE
#
# Function: classifies the ../website/ directory as a python package(enables import from main.py)
# About:
# - can hold multiple functions for init
# - contains the secret key for website
#


from venv import create
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

#creating database
db = SQLAlchemy()
DATABASE_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    #TODO store secret key in a seperate file that is ignored but gitignore (so people cant just look at the key on)
    app.config['SECRET_KEY'] = 'ihaveascendedtoavehicle'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DATABASE_NAME
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    #grabs blueprints
    from .views import viewsVar
    from .auth import authVar

    #registers blueprints
    app.register_blueprint(viewsVar, url_prefix='/')
    app.register_blueprint(authVar, url_prefix='/')


    #creates the database based on the the definitions in models.py
    from .models import User, Note
    create_database(app)

    return app

#creates the database IF AND ONLY IF it does not already exist
def create_database(app):
    if not path.exists('website/' + DATABASE_NAME):
        db.create_all(app=app)
        print('Database Created.')
