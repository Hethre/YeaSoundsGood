import os
from flask import Flask, render_template, redirect, request, session
from werkzeug.utils import secure_filename
from mongoengine import connect
from flask.ext.mongoengine import MongoEngine
import datetime

from models import User, Sound

DB_NAME = "soundsgood"
DB_USERNAME = "yeasoundsgooddev"
DB_PASSWORD = "yeas0undsg00d"
DB_HOST_ADDRESS = "ds035127.mongolab.com:35127/soundsgood"

UPLOAD_FOLDER = "data/uploads"
ALLOWED_EXTENSIONS = set(["wav"])

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

app.config["SECRET_KEY"] = "\xeeIm\n\xb4K\x8e\xfc\x1el\x9cj\xf7\x1a\xe9\xceQ\x80\xc7\x1e;\x01\xf9\xe5"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# database
app.config["MONGODB_DB"] = DB_NAME
connect(DB_NAME, host='mongodb://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST_ADDRESS)
db = MongoEngine(app)

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        file_name = file.filename
        sound = Sound.get_sound(file_name)
        if not sound:
          sound = Sound()
        file_type = file_name.rsplit(".", 1)[1]
        if file and "." in file_name and file_type in ALLOWED_EXTENSIONS:
          file_name = secure_filename(file_name)
          file.save(os.path.join(app.config["UPLOAD_FOLDER"], file_name))
          user = User.get_user(session["email"])
          sound.user = user
          sound.description = "this is a sound"
          sound.file_name = file_name
          sound.file_type = file_type
          sound.created = datetime.datetime.now()
          sound.save()
          return "/sound?file_name=%s" % file_name

    return render_template('upload.html')

@app.route("/sound", methods=["GET", "POST"])
def sound():
    if request.method == "GET":
        file_name = request.args["file_name"]
        sound = Sound.get_sound(file_name)
        if not sound:
            return render_template('404.html'), 404
        else:
            return render_template("sound.html", sound=sound)

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        # Create a brand new account.
        if request.form["submit"] == "Create":
            email = request.form["email"]
            # Make sure an email is provided.
            if not email:
                return render_template('404.html'), 404
            user = User.get_user(email)
            if not user:
                user = User()
                user.email = email
                user.password = "password"
                user.save()
                session["email"] = email
                sounds = user.get_sounds()
                return render_template("profile.html", sounds=sounds)
            else:
                return render_template('404.html'), 404
        # Log an existing user in.
        elif request.form["submit"] == "Login":
            email = request.form["email"]
            user = User.get_user(email)
            if not user:
                return render_template('404.html'), 404
            else:
                session["email"] = email
                sounds = user.get_sounds()
                return render_template("profile.html", sounds=sounds)
        # Log an existing user out.
        elif request.form["submit"] == "Logout":
            session["email"] = None
            return render_template('index.html')

        else:
            return render_template('404.html'), 404
    else:
      if session["email"]:
          user = User.get_user(session["email"])
          sounds = user.get_sounds()
          return render_template("profile.html", sounds=sounds)
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
