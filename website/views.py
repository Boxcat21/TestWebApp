# NOTES ABOUT FILE
# function: to run front-end visual stuff through python
#
#
from flask import Blueprint, render_template

viewsVar = Blueprint('viewsBlueprint', __name__)


@viewsVar.route('/')
def home():
    return render_template("home.html")