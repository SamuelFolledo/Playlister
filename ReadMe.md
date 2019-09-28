# [PLAYLISTER - VIDEO PLAYLISTS WITH FLASK AND MONGODB](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/start-a-flask-project)
You might have heard of the video site [YouTube](https://www.youtube.com) where millions of people have watched billions of hours of music, vlogs, how-tos, and of course, cats... acting like cats. We are going to piggyback on their success and create a YouTube Video Playlist app, aka Playlister, so that you can keep track of your favorites and share with your friends.


## To Run
- __1) Make sure you have Python installed__ - to check if you python, type python3 to the terminal and should see the following
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

--------------------------------------------------------------------------------------------------------
## Notes 
### [__1) MAKING A PLAN & STARTING A FLASK PROJECT__](https://www.makeschool.com/academy/track/standalone/playlistr-video-playlists-with-flask-and-mongodb-1c/start-a-flask-project)
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
