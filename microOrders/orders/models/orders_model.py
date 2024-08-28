from db.db import db
from sqlalchemy.sql import func

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(100), nullable=False)
    userEmail = db.Column(db.String(100), unique=True, nullable=False)
    saletotal = db.Column(db.Float, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, server_default=func.now())

    def __init__(self, userName, userEmail, saletotal):
        self.userName = userName
        self.userEmail = userEmail
        self.saletotal = saletotal
