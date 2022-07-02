# NOTES ABOUT FILE
# function: to run front-end visual stuff through python
#
#
from flask import Blueprint

viewsVar = Blueprint('viewsBlueprint', __name__)


@viewsVar.route('views')
def home():
    return '<h1>This is views.py, nothing exists</h1>'