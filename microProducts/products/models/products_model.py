from db.db import db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, unique=True, nullable=False)
    quantity = db.Column(db.Integer, unique=True, nullable=False)
    

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
