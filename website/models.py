# NOTES ABOUT FILE
# function: creates models for our database (THIS IS NOT THE DATABASE ITSELF)
#
#

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#in a database, each row is an element and each collumn is an attribute

#User Model
#NOTE: db.Model and UserMixin are not paramaters, this is inheritance syntax for python | class className(othClassName1, othClassName2)
class User(db.Model, UserMixin):
    #NOTE: db.String(number of characters)
    #primary key is unique identifier for each row, which is our id
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    user_name = db.Column(db.String(100))
    #plural because one-to-many relationship, one User table can map to multiple Note tables
    notes = db.relationship('Note')

    
#Note Model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #foreign key for column in User table
    #NOTE: a foreign key is a column in one table that refers to a column in a seperate table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))