import os
from flask import Flask, render_template, flash, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import LoginForm, RegistrationForm

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'book_manager'
app.config["MONGO_URI"] = 'mongodb+srv://root:<password>@myfirstcluster-x0xst.mongodb.net/book_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_reviews')
def get_tasks():
    return render_template("reviews.html", reviews=mongo.db.reviews.find())

@app.route('/book_gallery')
def get_tasks():
    return render_template("bookgallery.html")

@app.route('/get_users')
def get_users():
    return render_template("tasks.html", users=mongo.db.users.find())

@app.route('/add_book')
def get_tasks():
    return render_template("addbook.html")

@app.route('/login')
def get_tasks():
    return render_template("login.html")

@app.route('/signup')
def get_tasks():
    return render_template("signup.html")

@app.route('/landing_page')
def get_tasks():
    return render_template("index.html")

@app.route('/personal_account')
def get_tasks():
    return render_template("personalaccount.html")

@app.route('/reviews')
def get_tasks():
    return render_template("reviews.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=(os.environ.get('PORT')),
    debug=True)