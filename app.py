from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient()
db = client.Playlister
playlists = db.playlists



@app.route('/') #HOME
def playlists_index(): 
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists.find())


@app.route('/playlists/new') #NEW
def playlists_new(): 
    """Create a new playlist."""
    return render_template('playlists_new.html', playlist = {}, title = "New Playlist")


@app.route('/playlists', methods=['POST']) #SUBMIT
def playlists_submit():
    """Submit a new playlist."""
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split(),
        "rating": int(request.form.get("rating"))
    }
    playlist_id = playlists.insert_one(playlist).inserted_id #store the insert_id
    return redirect(url_for('playlists_show.html', playlist_id = playlist_id))

@app.route("/playlists/<playlist_id>") #SHOW
def playlists_show(playlist_id):
    """Show a single playlist"""
    playlist_id = playlists.find_one({"_id": ObjectId(playlist_id)})
    return render_template("playlists_show.html", playlist = playlist_id)

@app.route("/playlists/<playlist_id>/edit") #EDIT
def playlist_edit(playlist_id):
    """Show the edit form for a playlist."""
    playlist = playlists.find_one({"_id": ObjectId(playlist_id)})
    return render_template("playlists_edit.html", playlist = playlist, title = "Edit Playlist")

@app.route("/playlists/<playlist_id>", methods=["POST"]) #UPDATE
def playlists_update(playlist_id):
    """Submit an edited playlist. """
    updated_playlist = {
        "title": request.form.get("title"),
        "description": request.form.get("description"),
        "videos": request.form.get("videos").split(),
        "rating": int(request.form.get("rating"))
    }
    playlists.update_one(
        {"_id": ObjectId(playlist_id)},
        {"$set": updated_playlist})
    return redirect(url_for("playlists_show", playlist_id = playlist_id))

if __name__ == '__main__':
    app.run(debug=True)