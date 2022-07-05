# NOTES ABOUT FILE
#
# Function: authentication
# About:
# - outlines the url suffix of each webpage through a route-function matching
# - defines the http methods used on each page
#   - POST: requests that process information on the page
#   - GET: the default request that loads information onto the page
from flask import Blueprint, render_template, request, flash

authVar = Blueprint('authBlueprint', __name__)


@authVar.route('login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@authVar.route('logout')
def logout():
    return render_template("logout.html")

@authVar.route('sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        #retrieval of information
        email = request.form.get('email')
        userName = request.form.get('userName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #send user an error msg if basic checks not met
        if len(email) == 0 or len(userName) == 0 or len(password1) == 0:
            flash('User input has empty fields', category='error')
        elif password1 != password2:
            flash('User passwords do not match', category='error')
        else:
            flash('Account created', category='success')
            #checks passed, add the user to the database
            pass
        
        
    #baseline, show the default sign up page
    #implied GET request always
    return render_template("sign_up.html")