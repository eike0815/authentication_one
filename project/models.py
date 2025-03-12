from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email =  db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
