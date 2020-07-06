import os
from flask import (
    Flask, render_template, flash,
    redirect, request, url_for, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import LoginForm, RegistrationForm
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from os import path
if os.path.exists("env.py"):
  import env 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

'''
def hello():
    return "Hello world"
'''

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template("login.html", title='Sign In', form=form)
        # return redirect(url_for('book_gallery'))


@app.route('/landing_page')
def landing_page():
    return render_template("index.html")


@app.route('/get_reviews')
def get_reviews():
    reviews = mongo.db.reviews.find()
    return render_template("reviews.html", reviews=reviews)


@app.route('/book_gallery')
def book_gallery():
    return render_template("bookgallery.html")


@app.route('/get_users')
def get_users():
    users = mongo.db.users.find()
    return render_template("users.html", users=users)


@app.route('/add_book')
def add_book():
    return render_template("addbook.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('landing_page'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        return render_template("signup.html", form=form)
        # return redirect(url_for('book_gallery'))


@app.route('/personal_account')
def personal_account():
    return render_template("personalaccount.html")


@app.route('/reviews')
def reviews():
    return render_template("reviews.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)