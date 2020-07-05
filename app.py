import os
from flask import Flask, render_template, flash, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import LoginForm, RegistrationForm

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'book_manager'
#app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-x0xst.mongodb.net/book_manager?retryWrites=true&w=majority'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.secret_key = os.getenv('SECRET_KEY')

mongo = PyMongo(app)

@app.route('/')
@app.route('/landing_page')
def landing_page():
    return render_template("index.html")

@app.route('/get_reviews')
def get_reviews():
    return render_template("reviews.html", reviews=mongo.db.reviews.find())

@app.route('/book_gallery')
def book_gallery():
    return render_template("bookgallery.html")

@app.route('/get_users')
def get_users():
    return render_template("tasks.html", users=mongo.db.users.find())

@app.route('/add_book')
def add_book():
    return render_template("addbook.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('landing_page'))

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/personal_account')
def personal_account():
    return render_template("personalaccount.html")

@app.route('/reviews')
def reviews():
    return render_template("reviews.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=(os.environ.get('PORT')),
    debug=True)