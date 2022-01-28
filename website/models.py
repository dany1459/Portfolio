from . import db
from sqlalchemy.sql import func

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False)
    email = db.Column(db.String(150), unique=False)
    message = db.Column(db.String(5000), unique=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
