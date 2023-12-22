from app import app, api
from flask_restful import Resource, fields, marshal_with, abort,reqparse
from app.logic import ResponceTest, Registration, Authentication, Download


api.add_resource(ResponceTest, '/test')
api.add_resource(Registration, '/registr')
api.add_resource(Authentication, '/auth')
api.add_resource(Download, '/dwn')
