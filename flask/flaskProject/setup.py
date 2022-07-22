from flask import Flask, request
from flask_restful import Api
from main.settings import settings
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Integer, String
from serializers.product_serializer import ProductSerializer
from utils.responses import response_with
from utils import responses as resp
from flask_restful import Resource

app = Flask(__name__)
# Configuration
app.config.from_object(settings['development'])
db = SQLAlchemy(app)
db.init_app(app)


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


create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
db.create_all()
Migrate(app, db)

api = Api(app)


class Product(Resource):
    def get(self):
        product = ProductModel.query.all()
        author_schema = ProductSerializer()
        authors = author_schema.dump(product)
        return response_with(resp.SUCCESS_200, value={"authors": authors})

    def put(self, id):
        pass

    def patch(self, id):
        pass

    def delete(self, id):
        pass

    def post(self):
        try:
            data = request.get_json()
            author_schema = ProductSerializer()
            author = author_schema.load(data)
            result = author_schema.dump(author.create()).data
            return response_with(resp.SUCCESS_201, value={"author": result})
        except Exception as e:
            return response_with(resp.INVALID_INPUT_422)


api.add_resource(Product, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
