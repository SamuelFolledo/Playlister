# [PLAYLISTER - VIDEO PLAYLISTS WITH FLASK AND MONGODB](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/start-a-flask-project)
You might have heard of the video site [YouTube](https://www.youtube.com) where millions of people have watched billions of hours of music, vlogs, how-tos, and of course, cats... acting like cats. We are going to piggyback on their success and create a YouTube Video Playlist app, aka Playlister, so that you can keep track of your favorites and share with your friends.


## To Run
- __1) Make sure you have Python installed__ - to check if you python, type ```python3``` to the terminal and should see the following
```
$ python3
Python 3.5.2 (default, Nov 17 2016, 17:05:23)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>> _ 
```
- __Create a virtual environment__
```
$ cd playlister
$ python3 -m venv env
```
- __Activate the newly created virtual environment to install Python packages__
```
$ source env/bin/activate
```
- __Make sure Flask is installed in the virtual environment to get started with the project__
```
(env) $ pip3 install flask
```
- __To install packages from a requirements.txt file:__ 
```
$ pip3 install -r requirements.txt
```
- __To run the project__ 
```
(env) $ export FLASK_ENV=development; flask run
```
===============================

## Notes 
### [__PAGE 1) MAKING A PLAN & STARTING A FLASK PROJECT__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/start-a-flask-project)
- __Agile Sprints__ - updating often and adding more User Story to your software
- __User Story__ - term instead of "feature" to exmphasize the user's experience in their design, development, and testing which is called __User Centered Development__
- __Backlog__ - used to organize user stories and prioritze what you build and when
- __env__ directory which contains serveral sub-directories
    - ```$ python3 -m venv env``` We tell Python to execute the 'venv' module ('m' = 'module'), and put the resulting virtual environment in a directory called 'env'
- __activate__ - activates our newly created virtual environment so that we can use it to install our Python packages
    ```
    $ source env/bin/activate
    (env) $ _
    ```
- __deactivate__ - to deactivate the virtual environment, just type ```deactivate``` in terminal
- __pip freeze__ - let's us see all of the dependencies we have so far and stores it in a text file
    ```
    (env) $ pip3 freeze > requirements.txt
    ```
    - __re-run__ ```pip freeze``` command whenever you add or upgrade packages
    - __To install packages__ from the text file
        ```
        $ pip3 install -r requirements.txt
        ```
- __To run the project__ 
    ```
    (env) $ export FLASK_ENV=development; flask run
    ```
    - Navigate to ```http://localhost:5000```
- __.gitignore__ - a file which specifies any file types, files, or folders that we do not want to include in our Git repository. Write the following in our .gitignore file
    - ```env``` - is not necessary for anyone else who is reading or running this code, which is what requirements.txt file is for
    - ```__pycache__``` to ignore Python __generated files__ which are contained in pychache directory
----------------------------------------------------------

### [__PAGE 2) SEE ALL PLAYLISTS__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/index-playlists)
- __Resource__ is an abstract object that we use to organize data, code, and the features of our app
    - User resource to keep track of logging in and out, email and passwords, and people's birthdays
    - can also be related to each other
- __Resourcesful Routes__ - common actions all routes have

- Review this table of routes

| URL                 	| HTTP VERB 	| ACTION  	| WHAT IT DOES              	|
|:---------------------	|:-----------	|:---------	|:---------------------------	|
| /playlists          	| GET       	| index   	| See all playlists         	|
| /playlists/new      	| GET       	| new     	| See new playlist form     	|
| /playlists          	| POST      	| create  	| Create a new playlist     	|
| /playlists/:id      	| GET       	| show    	| See one playlist          	|
| /playlists/:id/edit 	| GET       	| edit    	| See an edit playlist form 	|
| /playlists/:id      	| PATCH/PUT 	| update  	| Update a playlist         	|
| /playlists/:id      	| DELETE    	| destroy 	| Delete a playlist         	|
----------------------------------------------------------


### [__PAGE 3) ADDING A MONGODB DATABASE TO YOUR APP__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/adding-mongodb)
- __JSON__ or __JavaScript Object Notation__ - a way to organize data to transmit it across the internet. It looks like a dictionary with key-value separated by a ```:``` and surrounded by a ```{ }```
- __[MongoDB database](https://www.mongodb.com)__ - allows you to save JSON just as they are as __key value pairs__
- __Single Document__ - what you call each object, which is why it is called a __document-based database__
- __collections__ - groups that these documents are collected into
- __\_id__ - a key which is a unique identifier number MongoDB gives each document
    - we can use this attribute to retrieve the whole document later
- __Installing MongoDB__ -
    - To install mongodb using homebrew
    ```
    $ brew update
    $ brew tap mongodb/brew
    $ brew install mongodb-community@4.2
    ```
    - __Also need to create a folder to save your databases on your computer__
    ```
    $ sudo mkdir -p /data/db
    ```
    - __Change owner__ if you have problems with permissions with this folder you can "change owner" of the directory using this command
    ```
    $ sudo mkdir -p /data/db
    ```
    - Need to __start the MongoDB daemon__ in order to user MongoDB and make it accessible frm your web server
    ```
    $ mongod # SHORT FOR "MONGO DAEMON"
    ```
- __[PyMongo](https://api.mongodb.com/python/current/) - A [MongoDB](https://www.mongodb.com) Library__ used to read MongoDB in our server code
    - __Install PyMongo__ library
    ```
    (env) $ pip3 install pymongo
    ```
    - Remember to run ```pip freeze > requirements.txt``` to update your list of installed packages!
    - __Initialize MongoDB in ```app.py``` and connect to our database that we'll name after our app
- ```find()``` - a method that returns an iteratable of all playlists in our database
    - call it in app.py when you call render_template()
----------------------------------------------------------

### [__PAGE 4) CREATE ROUTE: SAVING A NEW RESOURCE__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/creating-a-playlist)
- __POST__ - is a form method that submits/create a POST request to the url, ```/playlists```
    - Make sure we have the route that detechts post requests
- __For our server route to accepts a POST HTTP method__
    - Need to import from flask
        ```
        from flask import Flask, render_template, request, redirect, url_for
        ```
        - ```request.form``` - it is built-in in Flask which is needed to accept form data
            - gives us a dictionary containing the data that was sent in the page's HTML form. When you submit your form, you should see it log in in your terminal like this:
            ```
            { 'title': 'Creating a Playlist',
            'description': 'a sample playlist description' }
            ```
        - ```redirect``` and ```url_for``` which we'll use to redirect the user to another page on our site


----------------------------------------------------------

### [__PAGE 5) SHOW ROUTE: SEE ONE RESOURCE__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/showing-one-playlist)
- __show__ - action that give each single playlist its own page and unique url path
-----------------------------
| /playlists/:id      	| GET       	| show    	| See one playlist          	|
------------------
- __Url__ or __Request Parameter__ - using ```_id``` attribute for our ```:id``` in the route
    - we can access it in Flask using a paramter inside of the contoller route
- __Show on playlist__
    ```
    <!-- templates/playlists_index.html -->
    {% extends 'base.html' %}
    {% block content %}
        <h1>Playlists</h1>
        <a href="/playlists/new"> New Playlist</a>
        {% for playlist in playlists %}
            <h2><a href = "/playlists/{{playlist._id}}">{{playlist.title}}</a></h2>
            <small>{{ playlist.description }}</small>
        {% endfor %}
    {% endblock %}
    ```

    ```
    #in app.py
    @app.route("/playlists/<playlist_id>")
    def playlists_show(playlist_id):
    playlist_id = playlists.find_one({"_id": ObjectId(playlist_id)})
    return render_template("playlists_show.html", playlist = playlist_id)
    ```

- __Get a single playlist from MongoDB__


----------------------------------------------------------

### [__PAGE 6) EDIT ROUTE: EDITING AND UPDATING A RESOURCE__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/editing-and-deleting-a-playlist)


----------------------------------------------------------

### [__PAGE 7) DELETE ROUTE: DESTROYING A RESOURCE__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/deleting-a-playlist)


----------------------------------------------------------

### [__PAGE 8) ADDING TESTS__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/adding-tests)


----------------------------------------------------------

### [__PAGE 9) STYLING WITH BOOSTRAP__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/adding-bootstrap)


----------------------------------------------------------

### [__PAGE 10) PUSH TO PRODUCTION WITH HEROKU__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/push-to-heroku)


----------------------------------------------------------

### [__PAGE 11) ADDING COMMENTS__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/adding-comments)


----------------------------------------------------------

### [__PAGE 12) ADDING A ROUTE FOR COMMENTS__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/adding-route-for-comments)


----------------------------------------------------------

### [__PAGE 13) DELETE COMMENTS__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/deleting-comments)


----------------------------------------------------------

### [__PAGE 14) BELLS AND WHISTLES__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/bells-and-whistles)


----------------------------------------------------------

## Knowledge Outcomes
- Build a web app using [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/)
- Utilize a NoSQL database (MongoDB) for your web app
- Integrate RESTful and Resourceful routing in your web app
- CRUD a single resource
- Understand how to use Bootstrap for basic styling

## Credits:
- [Make School Courses](https://www.makeschool.com/academy)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) to build the web
- [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/) for templating
- [MongoDB](https://www.mongodb.com)
- [PyMongo](https://api.mongodb.com/python/current/)