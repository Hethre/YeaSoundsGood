import os
from flask import Flask, render_template, request
from mongoengine import connect
from flask.ext.mongoengine import MongoEngine

from models import User

DB_NAME = "soundsgood"
DB_USERNAME = "yeasoundsgooddev"
DB_PASSWORD = "yeas0undsg00d"
DB_HOST_ADDRESS = "ds035127.mongolab.com:35127/soundsgood"

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

app.config["SECRET_KEY"] = "\xeeIm\n\xb4K\x8e\xfc\x1el\x9cj\xf7\x1a\xe9\xceQ\x80\xc7\x1e;\x01\xf9\xe5"

# database
app.config["MONGODB_DB"] = DB_NAME
connect(DB_NAME, host='mongodb://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST_ADDRESS)
db = MongoEngine(app)

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        if request.form["submit"] == "Create":
            email = request.form["email"]
            return render_template("profile.html", email=email)
        elif request.form["submit"] == "Login":
            email = request.form["email"]
            return render_template("profile.html", email=email)
    else:
      return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
