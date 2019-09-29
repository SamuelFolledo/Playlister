from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient()
db = client.Playlister
playlists = db.playlists



@app.route('/')
def playlists_index(): 
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists.find())


@app.route('/playlists/new')
def playlists_new(): 
    """Create a new playlist."""
    return render_template('playlists_new.html')


@app.route('/playlists', methods=['POST'])
def playlists_submit():
    """Submit a new playlist."""
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split(),
        "rating": request.form.get("rating")
    }
    playlist_id = playlists.insert_one(playlist).inserted_id #store the insert_id
    return redirect(url_for('playlists_show', playlist_id = playlist_id))

@app.route("/playlists/<playlist_id>")
def playlists_show(playlist_id):
    """Show a single playlist"""
    playlist_id = playlists.find_one({"_id": ObjectId(playlist_id)})
    return render_template("playlists_show.html", playlist = playlist_id)

if __name__ == '__main__':
    app.run(debug=True)