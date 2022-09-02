from utils.db import db


class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, index=True)
    address = db.Column(db.String(256))
    phone = db.Column(db.String(30))
    email = db.Column(db.String(120), index=True)
    tracking_number = db.Column(db.String(24), index=True)


db.create_all()