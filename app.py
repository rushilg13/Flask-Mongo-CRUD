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

# Read Documents
@app.route('/home')
def index():
	user_list = mongo.db.users.find()
	return render_template("result.html",user_list=user_list)

# Helper function to handle BSON as MongoDB supports BSON
import json
from bson import ObjectId
from bson.objectid import ObjectId
import bson 

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

# Create Document
@app.route('/add', methods=["GET","POST"])
def add():
	form = AddForm()
	if form.validate_on_submit():
		fname_field = form.fname.data
		lname_field = form.lname.data
		phone_field = form.phone.data
		data = ({'fname':fname_field, 'lname':lname_field, 'phone': phone_field})
		user = mongo.db.users
		user.insert_one(data)
		return JSONEncoder().encode(data)
	return render_template("add.html", form = form)

# Update Page Route
@app.route('/updateform')
def updateform():
	id = request.args.get('id')
	user = mongo.db.users
	result_id = user.find_one({'_id':ObjectId(id)})
	form = AddForm(fname=result_id['fname'], lname=result_id['lname'], phone=result_id['phone'])
	return render_template("update.html", form=form, id = id)

# Update Document
from bson import json_util
@app.route('/update/<id>', methods=["POST"])
def update(id):
	user = mongo.db.users
	form = AddForm()
	if form.validate_on_submit():
		result = user.update_one({'_id':ObjectId(id)},{'$set':{'fname':form.fname.data, 'lname':form.lname.data, 'phone': form.phone.data}})
	return render_template("update.html",id=id,form=form)

# Delete Document
@app.route('/delete/<id>')
def delete(id):
	user = mongo.db.users
	delete_record = user.delete_one({'_id':ObjectId(id)})
	return redirect(url_for('index'))

# Contact Us Page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
	app.run(debug=True)