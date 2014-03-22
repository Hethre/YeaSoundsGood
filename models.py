from flask.ext.mongoengine import MongoEngine

db = MongoEngine()

class User(db.Document):
  email = db.StringField(required=True)
  password = db.StringField(required=True)

  @staticmethod
  def get_user(email):
    users_found = User.objects(email=email)
    if len(users_found) == 1:
      return users_found[0]
    elif len(users_found) == 0:
      return None
    else:
      raise Exception('Database Integrity Error')

class Sound(db.Document):
  user = db.ReferenceField(User)
  description = db.StringField()
  file_name = db.StringField()
  file_type = db.StringField()
  created = db.DateTimeField()
