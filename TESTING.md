# Testing
:electric_plug:

### Validators

* [W3C Markup Validation](https://validator.w3.org/)
    - Was used to check HTML5 validation.
    - Notes :memo: : Jinja syntax is not recognized.
* [W3C CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Was used to check CSS3 validation.
* [Esprima Syntax Validaton](https://esprima.org/index.html)
    - Was used to check Javascript validation.
* [Python syntax checker](https://extendsclass.com/python-tester.html)
    - Was used to check Python validation.
* [PEP online](http://pep8online.com/)
    - Was used to check PEP8 validation.
* [AutoPrefixer](https://autoprefixer.github.io/)
    - Was used to make sure that CSS3 was valid for all web browsers.
* [Google Search Console](https://autoprefixer.github.io/)
    - Was used to make sure that Responsive design worked on all devices.
https://search.google.com/test/mobile-friendly?hl=sv
* [Google Chrome](https://www.google.com/intl/sv/chrome/)
    - Was used to test the web browser.
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)
    - Was used to for debugging. 

## Features Testing

### Sign up , Login and Sign out
* __Testing__ :mag: : User fills the form with required inputs and submits the form. Testing 
that flash messages, redirection of page, werkzeug and connection to MongoDB works correctly. 
* __Result__ :hammer: : The user can sign up, login and sign out from the website, by navigating
and using the forms and links.
links
* __Passed__ :white_check_mark: : Testing passed the expected criterias 

### CRUD
* __Testing__ :mag: : Users can add, edit, update and delete books from the gallery. 
Testing that flash messages, python/flask syntax, modals, forms, redirection of page, connection to Mongo DB works correctly. 
* __Result__ :hammer: : The user can add, edit, update books from the gallery by filling in a form.
Users can also delete books by confirming on a modal, to delete a book.
* __Passed__ :white_check_mark: : Testing passed the expected criterias 

### Searchbox
* __Testing__ :mag: : Users can find a specific book, by typing in the searchbar and clicking on the button "search".
Testing that connection to MongoDB and buttons reset/search works correctly.  
* __Result__ :hammer: : searchbar works as expected. When searching for a book by typing for a specific book, the book
that the user search for, either is found or not. Also, reset button works, by resetting a search.
And connection to MongoDB works as expected.
* __Passed__ :white_check_mark: : Testing passed the expected criterias

### Social Media Icons
* __Testing__ :mag: : Users can use social media links to navigate to the websites specific social media account.
Testing that by clicking on social media link, the user gets navigated to the chosen social media account.
* __Result__ :hammer: : When clicking on social media icon, the user gets naviagated to the specific social media account. 
* __Passed__ :white_check_mark: : Testing passed the expected criterias 

### Responsive Design
* __Testing__ :mag: : Users can use different devices to navigate on the website.
Testing that the website works correctly on different devices and adjust on the responsive breakpoints.
* __Result__ :hammer: : The website is responsive on the different devices breakpoints and works correctly.
* __Passed__ :white_check_mark: : Testing passed the expected criterias 

## Bugs

### Sidenavbar
* __Bug__ :bug: : Side navbar was not working as expected. Menu icon was not showing up and when showing up
nothing happened when clicking on the menu icon.  
* __Resolved__ :key: : The bug was caused by having two different versions (1.0.0) of Materialize, when
resolving this bug by implementing the same versions of Materialize, the side navbar worked correctly.
`<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css">`
`<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>`
* __Passed__ :white_check_mark: :
`code`

### Responsive design
* __Bug__ :bug: : Had some bugs ith the responsive design and some parts of the pages, were crashing and
did not follow the grid breakpoints 
* __Resolved__ :key: : Started to implement and follow the [Materialize grid system](https://materializecss.com/grid.html) everywhere on the website, as I should
have done from the beginning.
* __Passed__ :white_check_mark: :

### CRUD
* __Bug__ :bug: : CRUD had some bugs along the way. Problems with connecting with MongoDB.
* __Resolved__ :key: : Was able to solve the problem by using and following the [MongoDB documentation](https://docs.mongodb.com/).
* __Passed__ :white_check_mark: 

### Login, Signup, Sign out
* __Bug__ :bug: : Had several bugs with the process of login, sign up and sign out. Tried first with WTForms and
was not able to make it work. Also connection with MongoDB was not working.
* __Resolved__ :key: : Was able to solve the problem with the forms, by using the [werkzeug documentation](https://jinja.palletsprojects.com/en/2.11.x/). 
```from werkzeug.security import generate_password_hash, check_password_hash```.
Also figured out how to solve the syntax to connect properely to MongoDB, by using the [MongoDB documentation](https://docs.mongodb.com/).
* __Passed__ :white_check_mark: 

### Materialize
* __Bug__ :bug: : jQuery code from Materialize, as side navbar, tooltip and modal was not working as expected. 
* __Resolved__ :key: : The bug was caused by having two different versions (1.0.0) of Materialize, when
resolving this bug by implementing the same versions of Materialize, all the jQuery code from Materialize worked correctly.
`<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css">`
`<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>`
* __Passed__ :white_check_mark: 