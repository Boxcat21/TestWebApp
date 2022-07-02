# NOTES ABOUT FILE
#
# Function: authentication
# 
# 
#
from flask import Blueprint

authVar = Blueprint('authBlueprint', __name__)


@authVar.route('login')
def login():
    return '<h1>login page</h1>'

@authVar.route('logout')
def logout():
    return '<h1>logout page</h1>'

@authVar.route('sign_up')
def sign_up():
    return '<h1>sign up page</h1>'