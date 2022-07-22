from main.database import serializer
from marshmallow import fields
from models.products import ProductModel


class ProductSerializer(serializer.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        load_instance = True

    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    price = fields.Integer(required=True)
