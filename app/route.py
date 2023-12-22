from app import app, api
from flask_restful import Resource, fields, marshal_with, abort,reqparse
from app.logic import ResponceTest


api.add_resource(ResponceTest, '/test')
