from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Mohammed"}
    posts = [
        {
            "author": {'username': 'Ghita'},
            "body": 'Beautiful day in Switzrland'
        },
        {
            "author": {"username": "Susan"},
            "body": "The avengers movie was Cool!"
        }
    ]
    return render_template("index.html", user=user, posts=posts, title="Home")
