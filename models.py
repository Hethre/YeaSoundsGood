from flask.ext.mongoengine import MongoEngine

db = MongoEngine()

class User(db.Document):
  email = db.StringField(required=True)
  password = db.StringField(required=True)
