from .dbinitialization import db

class teacher(db.Document):
    name = db.StringField(required=True)
    empcode = db.StringField(required=True)
    exp = db.FloatField()
    edu = db.StringField()