# Importing Library
from flask import Flask, render_template,url_for, redirect, jsonify, request, session
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
from flask_pymongo import PyMongo
import os

app= Flask(__name__)

# Database name here
app.config["MONGO_DBNAME"] = 'SwiftSkuINC'

# Declare Secret Key and MongoURI
app.config["MONGO_URI"] = 'mongodb://127.0.0.1:27017/SwiftSkuINC'
app.config['SECRET_KEY'] = os.urandom(24)

mongo = PyMongo(app)

# Using WTForms class to handle create and update requests
class AddForm(FlaskForm):
	fname = StringField('fname', validators = [InputRequired()])
	lname = StringField('lname', validators = [InputRequired()])
	phone = StringField('phone', validators = [InputRequired()])