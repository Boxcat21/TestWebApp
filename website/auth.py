# NOTES ABOUT FILE
#
# Function: authentication
# 
# 
#
from flask import Blueprint, render_template

authVar = Blueprint('authBlueprint', __name__)


@authVar.route('login')
def login():
    return render_template("login.html")

@authVar.route('logout')
def logout():
    return render_template("logout.html")

@authVar.route('sign_up')
def sign_up():
    return render_template("sign_up.html")