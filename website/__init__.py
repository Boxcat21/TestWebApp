# NOTES ABOUT FILE
#
# Function: classifies the ../website/ directory as a python package(enables import from main.py)
# About:
# - can hold multiple functions for init
# - contains the secret key for website
#


from flask import Flask

def create_app():
    app = Flask(__name__)
    #TODO store secret key in a seperate file that is ignored but gitignore (so people cant just look at the key on)
    app.config['SECRET_KEY'] = 'ihaveascendedtoavehicle'

    #grabs blueprints
    from .views import viewsVar
    from .auth import authVar

    #registers blueprints
    app.register_blueprint(viewsVar, url_prefix='/')
    app.register_blueprint(authVar, url_prefix='/')


    return app