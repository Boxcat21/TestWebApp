# NOTES ABOUT FILE
#
# Function: authentication
# About:
# - outlines the url suffix of each webpage through a route-function matching
# - defines the http methods used on each page
#   - POST: requests that process information on the page
#   - GET: the default request that loads information onto the page
from flask import Blueprint, redirect, render_template, request, flash, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

authVar = Blueprint('authBlueprint', __name__)


@authVar.route('login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('login successful.', category='success')
                return redirect(url_for('viewsBlueprint.home'))
            else:
                flash('login unsuccessful, incorrect password', category='error')
        else:
            flash('login unsuccessful, email does not exist', category='error')

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
        elif User.query.filter_by(email=email).first():
            #email already exists
            flash('email already exists, try again', category='error')
        elif User.query.filter_by(user_name=userName).first():
            #username already exists
            flash('username already exists, try again', category='error')
        else:
            #checks passed, add the user to the database
            new_user = User(email=email, user_name=userName, password=generate_password_hash(password1, method='sha256'))

            db.session.add(new_user)
            db.session.commit()

            flash('Account created', category='success')
            return redirect(url_for('authBlueprint.login'))
            
        
    #baseline, show the default sign up page
    #implied GET request always
    return render_template("sign_up.html")