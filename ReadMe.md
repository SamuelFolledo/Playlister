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
| URL                 	| HTTP VERB 	| ACTION  	| WHAT IT DOES              	|
|---------------------	|-----------	|---------	|---------------------------	|
| /playlists          	| GET       	| index   	| See all playlists         	|
| /playlists/new      	| GET       	| new     	| See new playlist form     	|
| /playlists          	| POST      	| create  	| Create a new playlist     	|
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

| URL                 	| HTTP VERB 	| ACTION  	| WHAT IT DOES              	|
|---------------------	|-----------	|---------	|---------------------------	|
| /playlists/:id      	| GET       	| show    	| See one playlist          	|

- __Url__ or __Request Parameter__ - using ```_id``` attribute for our ```:id``` in the route
    - we can access it in Flask using a paramter inside of the contoller route
- __Show one playlist__
    - In templates/playlists_index.html
        ```
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
    - In app.py
        ```
        from flask import Flask, render_template, request, redirect, url_for
        ...
        @app.route("/playlists/<playlist_id>")
        def playlists_show(playlist_id):
        playlist_id = playlists.find_one({"_id": ObjectId(playlist_id)})
        return render_template("playlists_show.html", playlist = playlist_id)
        ```



----------------------------------------------------------

### [__PAGE 6) EDIT ROUTE: EDITING AND UPDATING A RESOURCE__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/editing-and-deleting-a-playlist)
| URL                 	| HTTP VERB 	| ACTION  	| WHAT IT DOES              	|
|---------------------	|-----------	|---------	|---------------------------	|
| /playlists          	| GET       	| edit   	| See an edit playlist form    	|
| /playlists/new      	| PUT/PATCH     | update    | Update playlist               |
- __Edit and Update__ are similar to New and Create. 
    - 1) Need a link to the edit route that renders ```playlists_edit``` template
    - 2) Submit that edit form to the update route which will redirect to the show action
- __PUT vs. POST__ - although our update action will be expecting a PUT HTTP action, HTML forms cannot take an action attribute of ```PUT```. Therefore, we'll make it a ```POST``` action instead
- ```value = ' '``` = we are using the ```value``` html attribute to pass in the values of the playlist we are trying to edit
- ```<textarea>{{ }}</textarea>``` - the <textarea> HTML tag does not have a value attribute, so its contents must go between its open and close tags
- In ```app.py```:
```
    @app.route("/playlists/<playlist_id>/edit") #EDIT
    def playlist_edit(playlist_id):
        playlist = playlists.find_one({"_id": ObjectId(playlist_id)})
        return render_template("playlists_edit.html", playlist = playlist, title = "Edit Playlist")

    @app.route("/playlists/<playlist_id>", methods=["POST"]) #UPDATE
    def playlists_update(playlist_id):
        updated_playlist = { "title": request.form.get("title"), "description": request.form.get("description"), "videos": request.form.get("videos").split(), "rating": int(request.form.get("rating"))}
        playlists.update_one(
            {"_id": ObjectId(playlist_id)},
            {"$set": updated_playlist})
        return redirect(url_for("playlists_show", playlist_id = playlist_id))
```
- In ```templates/playlists_show.html```:
    ```
    <form method='POST' action='/playlists'>
        {% include 'partials/playlists_form.html' %}
    </form>
    ```
- Add a ```templates/playlists_edit.html``` template:
    ```
    <form method='POST' action='/playlists/{{playlist._id}}'>
        {% include 'partials/playlists_form.html' %}
    </form>
    ```
- Create a partials folder inside templates folder and create ```playlists_form.html```
    ```
    <fieldset>
        <legend>{{ title }}</legend>
        <!-- TITLE -->
        <p>
            <label for='playlist-title'>Title</label><br>
            <input id='playlist-title' type='text' name='title' value='{{ playlist.title }}'/>
        </p>

        <!-- DESCRIPTION -->
        <p>
            <label for='description'>Description</label><br>
            <input id='description' type='text' name='description' value='{{ playlist.description }}' />
        </p>

        <!-- VIDEO LINKS -->
        <p>
            <label for='playlist-videos'>Videos</label><br>
            <p>Add videos in the form of 'https://youtube.com/embed/KEY'. Separate with a newline.</p>
            <textarea id='playlist-videos' name='videos' rows='10' />{{ "\n".join(playlist.videos) }}</textarea>
        </p>
    </fieldset>

    <!-- BUTTON -->
    <p>
        <button type='submit'>Save Playlist</button>
    </p>

    ```

- __Partial Template__ - pulling a code out into its own template
    - __To put a file from partials folder__ put this in an HTML file you want it to appear at
        ```
        {% include "partials/playlists_form.html" %}
        ```
    

----------------------------------------------------------

### [__PAGE 7) DELETE ROUTE: DESTROYING A RESOURCE__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/deleting-a-playlist)
| URL                 	| HTTP VERB 	| ACTION  	| WHAT IT DOES              	|
|---------------------	|-----------	|---------	|---------------------------	|
| /playlists          	| DELETE       	| Destroy   | Delete a playlist         	|

- __To Delete from db using _id__-
    ```
    playlists.delete_one({'_id': ObjectId(playlist_id)})
    ```
- __NOTE__
    - __render_template__ expects an __.html file__
        ```
        return render_template('playlists_edit.html', playlist = playlist, title = 'Edit Playlist')
        ```
    - __redirect(url_for())__ expects a function name in ```app.py```
        ```
        return redirect(url_for('playlists_show', playlist_id = playlist_id))
        ```

----------------------------------------------------------

### [__PAGE 8) ADDING TESTS__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/adding-tests)
- __unittest__ - use for Unit Testing Framework to run our tests
- __unittest.mock__ - to mock out sample data
- __Manual Testing__ - tests if your code is working manually
- __Regression Test__ - what happens to old tests, and act as sort of a double check that new code didn't break old stuff
- __Asserts__ - used to check whether we receive the data correctly and what we expect to see from the test Flask client
- __[unittest](https://docs.python.org/3/library/unittest.html#unittest.TestCase)__ - frame work that has many different assert methods like:

| Method                    	| Checks that          	|
|---------------------------	|----------------------	|
| assertEqual(a, b)         	| a == b               	|
| assertNotEqual(a, b)      	| a != b               	|
| assertTrue(x)             	| bool(x) is True      	|
| assertFalse(x)            	| bool(x) is False     	|
| assertIs(a, b)            	| a is b               	|
| assertIsNot(a, b)         	| a is not b           	|
| assertIsNone(x)           	| x is None            	|
| assertIsNotNone(x)        	| x is not None        	|
| assertIn(a, b)            	| a in b               	|
| assertNotIn(a, b)         	| a not in b           	|
| assertIsInstance(a, b)    	| isinstance(a, b)     	|
| assertNotIsInstance(a, b) 	| not isinstance(a, b) 	|

- __Sample of tests.py__
    ```
    from unittest import TestCase, main as unittest_main
    from app import app
    class PlaylistsTests(TestCase):
        def setUp(self):
            self.client = app.test_client() #Get the Flask test client
            app.config['TESTING'] = True # Show Flask errors that happen during tests

        def test_index(self): #test to see that index page loads with a status of 200 and the data
            result = self.client.get('/')
            self.assertEqual(result.status, '200 OK')
            self.assertIn(b'Playlist', result.data)

    if __name__ == '__main__':
        unittest_main()
    ```
- ```unittest.mock``` - use to send mock data to our rotes instead of using actual data on PyMongo servers
- __mock decorator__ - tells our test function that we'll be using a fake version of PyMongo's find_one operation

```
from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from app import app

sample_playlist_id = ObjectId('5d55cffc4a3d4031f42827a3')
sample_playlist = {
    'title': 'Cat Videos',
    'description': 'Cats acting weird',
    'videos': [
        'https://youtube.com/embed/hY7m5jjJ9mM',
        'https://www.youtube.com/embed/CQ85sUNBK7w'
    ],
    'rating': 4
}
sample_form_data = {'title': sample_playlist['title'],
    'description': sample_playlist['description'],
    'videos': '\n'.join(sample_playlist['videos']),
    'rating': 4
}

class PlaylistsTests(TestCase):
    def setUp(self): #set up
        self.client = app.test_client() #Get the Flask test client
        app.config['TESTING'] = True # Show Flask errors that happen during tests

    def test_index(self):
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Playlist', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_playlist(self, mock_find):
        """Test showing a single playlist."""
        mock_find.return_value = sample_playlist
        result = self.client.get(f'/playlists/{sample_playlist_id}')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Cat Videos', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_edit_playlist(self, mock_find):
        mock_find.return_value = sample_playlist
        result = self.client.get(f'/playlists/{sample_playlist_id}/edit')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Cat Videos', result.data)

    @mock.patch('pymongo.collection.Collection.insert_one')
    def test_submit_playlist(self, mock_insert):
        result = self.client.post('/playlists', data=sample_form_data)
        # After submitting, should redirect to that playlist's page
        self.assertEqual(result.status, '302 FOUND')
        mock_insert.assert_called_with(sample_playlist)

    @mock.patch('pymongo.collection.Collection.update_one')
    def test_update_playlist(self, mock_update):
        result = self.client.post(f'/playlists/{sample_playlist_id}', data=sample_form_data)
        self.assertEqual(result.status, '302 FOUND')
        mock_update.assert_called_with({'_id': sample_playlist_id}, {'$set': sample_playlist})

    @mock.patch('pymongo.collection.Collection.delete_one')
    def test_delete_playlist(self, mock_delete):
        form_data = {'_method': 'DELETE'}
        result = self.client.post(f'/playlists/{sample_playlist_id}/delete', data=form_data)
        self.assertEqual(result.status, '302 FOUND')
        mock_delete.assert_called_with({'_id': sample_playlist_id})

if __name__ == '__main__':
    unittest_main()
```
----------------------------------------------------------

### [__PAGE 9) STYLING WITH BOOSTRAP__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/adding-bootstrap)
- __Bootstrap__ - web's most populat CSS Framework with the following elements: _grid, navbar, forms, inputs, buttons_
- __Responsive__ - Bootstrap's grid system is responsive, meaning it changes depending on the size of the screen that is being shown on


----------------------------------------------------------

### [__PAGE 10) PUSH TO PRODUCTION WITH HEROKU__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/push-to-heroku)
- __[Heroku](https://www.heroku.com)__ - help us make our website live
- __[Heroku Command Line Interface (CLI)](https://devcenter.heroku.com/articles/heroku-cli)__ - makes it easy to create and manage your Heroku apps directly from the terminal. It’s an essential part of using Heroku
- __gunicorn__ - a _multi-threaded_ web server which allows our server to perform well when multiple users make requests unlike Flask which is a _single-threaded_ web server
- __Procfile__ special file that lets Heroku know how to run your website
    ```
    $ touch Procfile
    ```
    - Paste this to Procfile
        ```
        web: gunicorn app:app
        ```
- create a heroku app named ("Playlister-sf") ```//sf being your initial```
- This ```heroku create``` command will add our heroku app as a git remote repository that we will be able to ```git push```. We can see our remote repos - ```git remote -v```
    ``` 
    $ heroku create playlister-MY-INITIALS
    $ git remote -v
    ```
- Push to Heroku!
    ```
    $ git push heroku master
    $ heroku open
    ```
- ```ps:scale``` - additional command needed to run that tells Heroku to assign a free worker to our deployment in order to run your website
    - just like ```heroku create```, you only need to execute this command once per project
    ```
    $ heroku ps:scale web=1
    ```
- Whenever you have an error or problem with Heroky, see the logs by running
    ```
    $ heroku logs
    ```
    - to see continually add a tail
        ```
        $ heroku logs --tail
        ```
- __Adding a Production Database__ 
    - Add [mLabs](https://mlab.com), ```mLabs``` is a mongodb heroku add-on that is needed because ```'mongodb://localhost/Playlister'``` URI is in our local computer, and heroku is remote and doesn't have access to that
        ```
        $ heroku addons:create mongolab:sandbox
        ```
    - Then we have to point to this production mongodb database URI in our ```app.py``` file and use ```os.environ.get``` to get the ```MONGODB_URI``` __environment variable__
        ```
        # app.py
        import os
        ...
        host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Playlister')
        client = MongoClient(host=host)
        db = client.get_default_database()
        playlists = db.playlists
        ```
    - You may need to add ```?retryWrites=false``` to your MongoDB URL. so change 'host=' line above to:
        ```
        client = MongoClient(host=f'{host}?retryWrites=false')
        ```
    - Since Heroku does not use port 5000, it uses another port available in production at the environment variable ```PORT``` just like your mongoDB URI.
        - fix that by setting the port also with the ```os.environ.get```. Then we have to point to this production mongodb database URI in our ```app.py``` file
            ```
            # app.py
            if __name__ == '__main__':
            app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
            ```



----------------------------------------------------------

### [__PAGE 11) ADDING COMMENTS__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/adding-comments)

----------------------------------------------------------

### [__PAGE 12) ADDING A ROUTE FOR COMMENTS__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/adding-route-for-comments)
- __Associate__ - keeping track of this relationship
- The comment will be __child__ to the __parent__ playlist
- __hidden form field__ - an input tag that has a value that isn't visible in the browser
- __What just happened?__
    - You created a relationship between two different document/records in your database. Playlists each have a unique id. By saving the id of a Playlist with a Comment, comments can find the Playlist that they are are associated with. Playlists can also find all of the Comments that are associated with their id.

    - This is a __one to many relationship__. This an important concept in database design, and an important tool you will use when managing data.

----------------------------------------------------------

### [__PAGE 13) DELETE COMMENTS__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/deleting-comments)


----------------------------------------------------------

### [__PAGE 14) BELLS AND WHISTLES__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/bells-and-whistles)
- __[Bootswatch](https://bootswatch.com)__ - to customize style a little bit more with a free bootstrap theme

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