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

  def get_sounds(self):
    sounds_found = Sound.objects(user=self)
    return sounds_found

class Sound(db.Document):
  user = db.ReferenceField(User)
  description = db.StringField()
  file_name = db.StringField()
  file_type = db.StringField()
  created = db.DateTimeField()

  @staticmethod
  def get_sound(file_name):
    sounds_found = Sound.objects(file_name=file_name)
    if len(sounds_found) == 1:
      return sounds_found[0]
    elif len(sounds_found) == 0:
      return None
    else:
      raise Exception('Database Integrity Error')
