import os
from flask import Flask, render_template, flash, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from os import path
if os.path.exists("env.py"):
    import env 


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'book_manager' 
app.config['MONGO_URI'] = os.environ['MONGO_URI']  
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/reviews')
def reviews():
    reviews = mongo.db.reviews.find()
    return render_template("reviews.html", reviews=reviews)


@app.route('/gallery')
def gallery():
    return render_template("bookgallery.html", reviews=mongo.db.reviews.find())

@app.route('/book')
def book():
    return render_template("addbook.html")


@app.route('/add_book', methods=['POST'])
def add_book():
    reviews =  mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('gallery'))

@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("editreview.html", review=review)

@app.route('/update_review/<review_id>', methods=["POST"])
def update_review(review_id):
    review = mongo.db.reviews
    review.update({'_id': ObjectId(review_id)},
    {
        'title': request.form.get('title'),
        'author': request.form.get('author'),
        'description': request.form.get('description'),
        'cover_url': request.form.get('cover_url'),
        'amazon_url': request.form.get('amazon_url')
    })
    return redirect(url_for('gallery'))
    
#flash('Review Updated ', 'success')
#flash(('The book has been successfully deleted').format(book_id),'success')

@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('gallery'))

@app.route('/users')
def users():
    users = mongo.db.users.find()
    return render_template("users.html", users=users)

@app.route('/login', methods=['GET', 'POST'])
def login():
        username = request.form.get('username')
        password = request.form.get("password")
        reg_user = find_user(username)
        if reg_user and check_password_hash(reg_user["password"], password):
        #flash('You have been logged in!', 'success')
         session["user"] = username
        return redirect(url_for('gallery', username=session["user"]))
   # else:
       # flash('Login unsuccessful. Please try again', 'danger')
        return render_template("login.html", title='Sign In', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        req = request.form

        username = req.get('username')
        email = req.get('email')
        password = req.get("password")
        flash('You have been successfully logged out!')
        return redirect(url_for('gallery'))

    return render_template("signup.html")

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been successfully logged out!', 'success')
    return redirect(url_for('landing_page'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
