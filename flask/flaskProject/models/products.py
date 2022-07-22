from sqlalchemy import Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ProductModel(db.Model):
    """
    This is a base product Model
    """
    __tablename__ = 'product'

    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(100), nullable=False)
    price = db.Column(Integer, nullable=False)

    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __repr__(self):
        return "<Product(title='%s', price='%i')>" % (self.title, self.price)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
