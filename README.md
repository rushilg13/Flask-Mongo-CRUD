# Simple CRUD-Web using MongoDB and Flask

This is a simple phone book application with CRUD operations using MongoDB and Flask.
The Database Management System is MongoDB. 
The python-MongoDB connector is PyMongo.

### Installation

First, you should [install MongoDB](https://docs.mongodb.com/manual/installation/)

then install all dependencies by running the following command:

```
$ sudo pip install -r requirements.txt
```

It will install Flask, Flask-WTF, and PyMongo.

### Usage

To run the program, first you should make sure MongoDB is running, start it using:

```
$ sudo service mongod start
```

then, run the program:

```
$ python app.py
```

Open your browser and go to `localhost:5000	` to see the running program.