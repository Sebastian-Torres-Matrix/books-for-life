# BOOKS FOR LIFE
![Multi Device Website Mockup](static/images/mockup-min.png)
:books: Visit the live website: [Books For Life](https://books-for-life.herokuapp.com/)

## Introduction 
Welcome to Books For Life!

## Table of Contents
* [UX](#ux)
    * [Project Goals](#project-goals)
    * [User Stories](#user-stories)
    * [Design Choices](#design-choices)
    * [Wireframes](#wireframes)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features Left to Implement](#features-left-to-implement)
* [Technologies Used](#technologies-used)
    * [Tools](#tools)

* [Testing](#testing)

* [Deployment](#deployment)

* [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)

* [Disclaimer](#disclaimer)

## UX 

#### Project Goals :dart: 
The aim of the project is to create a book website where users can search and find books that they want to read, 
books that they already have read and want to give a review or save as a favorite on their personal account,
also the user can buy the book through an affiliate link.

#### Site Owner Goals:
* Provide a platform for book lovers to find books they like
* Earn money on each book purchased via a affiliate link from the website.
* Collect user information through site analytics to optimize the website for users

#### User Stories :clapper: 
* I want to be able to create a personal account
* I want to be able to delete my personal account
* I want to be able to save my favorite books on my personal account
* I want to be able to see book reviews from other users
* I want to see how popular the book is, through thumbs up or thumbs down
* I want to be able to search books by genre
* I want to see the book title, cover of the book and the author name
* I want to be able to buy the book by using a link that takes my to a book shop
* I want to be able to delete or edit my reviews
* I want to be able to sign out
* I want the website to responsive on my laptop, iPad and mobile phone


#### Design Choices :art:

* __Icons__
Are being applied from Font Awesome. That has a large collection to choose from. 

* __Colors__
* Wheat colour: #E8D0A9
* White colour: #FFF

#### Wireframes
* The wireframes were created using [Balsamiq](https://balsamiq.com/).
    * Here is the link to see the [Wireframes]()

#### Databases

Users Collection
ID | Data Type
------------- | -------------
_id | Int
username | String
email | String

Reviews Collection
ID | Data Type
------------ | -------------
_id | Int
title | String
author | String
genre | String
upvote | Array
downvote | Array
upvote_total | Int
downvote_total | Int


## Features :mag_right:

#### Existing Features
* Users can create a personal account, with a unique username to login, add books and leave book reviews
* Users can delete their profile account if they wish to do so
* Users can sign in and also sign out
* Users can add books on the website
* Users can add, edit and delete book reviews
* Users can save favorite books to their personal account
* Users can choose book gallery based on genre
* Users can buy books through link to Amazon

#### Features Left to Implement


## Technologies Used :computer: 

#### Languages
* HTML
* CSS 
* JavaScript 
* Python

#### Libaries & Frameworks
* [Flask](https://flask.palletsprojects.com/en/1.1.x/ ) 
* [Bootstrap](https://getbootstrap.com/) 
* [FontAwesome](https://fontawesome.com/)  
* [JQuery](https://jquery.com/) 

#### Databases
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)

#### Tools :wrench:
* [Balsamiq](https://balsamiq.com/) 
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) 
* [Git](https://git-scm.com/) 
* [Github](https://github.com/) 
* [Gitpod](https://www.gitpod.io/) 
* [Google Fonts](https://fonts.google.com/)
* [Heroku](https://dashboard.heroku.com/apps)
* [Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/) 

## Testing :electric_plug:

## Deployment

## Credits 

#### Content

    
#### Media


#### Acknowledgements

 
## Disclaimer 
* The content of this website is for educational purpose only. :heavy_exclamation_mark:

## Back to the top 
* [Table of Contents](#table-of-contents) :arrow_up:
