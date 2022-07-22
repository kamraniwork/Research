# from flask_restful import Resource
# from flask import Blueprint, request, url_for, current_app
# from utils.responses import response_with
# from utils import responses as resp
# # from models.products import ProductModel
# from setup import ProductModel
# from serializers.product_serializer import ProductSerializer
#
#
# class Product(Resource):
#     def get(self):
#         product = ProductModel.query.all()
#         author_schema = ProductSerializer()
#         authors, error = author_schema.dump(product)
#         return response_with(resp.SUCCESS_200, value={"authors": authors})
#
#     def put(self, id):
#         pass
#
#     def patch(self, id):
#         pass
#
#     def delete(self, id):
#         pass
