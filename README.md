# BOOKS FOR LIFE :books:
![Multi Device Website Mockup](static/images/mockup-min.png)
Visit the live website: [Books For Life](https://books-for-life.herokuapp.com/)

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
password | String

Reviews Collection
ID | Data Type
------------ | -------------
_id | Int
title | String
author | String
description | String
cover_url | String
amazon_url | String


## Features :mag_right:

#### Existing Features
* Users can sign up to Books for Life, with a unique username and password
* Users can log in to the website, with their unique username and password
* Users can sign out from the website
* Users can create and add books to the book gallery
* Users can edit and update existing book reviews
* Users can delete existing books from the book gallery
* Users can search for specific books in the book gallery
* Users can buy books through a Amazon link 
* Users can follow Books for Life through social media, via social media icons

#### Features Left to Implement
* The ability to sort books in the gallery
* Choose books by genre
* Upvote books or/and save books as favorites
* Have a personal account, with personal information, details and favorite books
* Reset password and create a new password
* Input email and send newsletter to users email account
* Pagination when there are many books accumulated in the gallery 

## Technologies Used :computer: 

#### Languages
* HTML
* CSS 
* JavaScript 
* Python

#### Libaries & Frameworks
* [Flask](https://flask.palletsprojects.com/en/1.1.x/ ) 
* [Materialize](https://materializecss.com/) 
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
* [Am I Responsive?](http://ami.responsivedesign.is/#) 

## Testing :electric_plug:

## Deployment

## Credits 

#### Content
* These websites, for the excellent content, with explanations and tutorials:
    * [StackOverflow](https://stackoverflow.com/)
    * [W3Schools](https://www.w3schools.com/)
    * [MongoDB Documentation](https://docs.mongodb.com/)
    * [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)
    * [Jinja Documentation](https://jinja.palletsprojects.com/en/2.11.x/)
 
#### Media
* [Favicon.io](https://favicon.io/)
    * For the favicon used in the project.
* [Optimizilla](https://imagecompressor.com/)
    * Image compressor to shrink JPEG and PNG images. 
* [Pexels](https://www.pexels.com/photo/assorted-books-on-shelf-1370295/) 
    * For the embedded background image used in the project.

#### Acknowledgements
* Fellow Code Institute students on [Slack](https://slack.com/intl/en-se/). For the support and feedback.
* Tutor support and Student care from Code Institute. For the support, guidance and feedback.
* [Simen Daehlin](https://dehlin.dev/), for excellent mentorship, with great guidance and feedback. :trophy:
    * [Github](https://github.com/Eventyret)
    * [Linkedin](https://uk.linkedin.com/in/simendaehlin)
 
## Disclaimer 
* The content of this website is for educational purpose only. :heavy_exclamation_mark:

## Back to the top 
* [Table of Contents](#table-of-contents) :arrow_up:
