from app import app, api
from flask_restful import Resource, fields, marshal_with, abort,reqparse
from logic import ResponceTest

print("hello")
task_post_args = reqparse.RequestParser()
task_post_args.add_argument("text_question",type=str,help="Task is text_question", required= True )

api.add_resource(ResponceTest, '/test')
