from app import app, api
from flask_restful import Resource, fields, marshal_with, abort,reqparse

print("hello")
task_post_args = reqparse.RequestParser()
task_post_args.add_argument("text_question",type=str,help="Task is text_question", required= True )

class RespoceTest(Resource):
    def post(self):
        print("hello")
        args = task_post_args.parse_args()
        print(args['text_question'])
        return 200

api.add_resource(RespoceTest, '/test')
