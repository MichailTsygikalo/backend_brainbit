from flask_restful import Resource, fields, marshal_with, abort,reqparse
from flask import make_response, send_file, jsonify,request
from app import db
import json
import random
import time
from app.model import User
print("hello")
task_post_args = reqparse.RequestParser()
task_post_args.add_argument("text_question",type=str,help="Task is text_question", required= True )

class ResponceTest(Resource):
    def post(self):
        print("hello")
        args = task_post_args.parse_args()
        print(args['text_question'])
        return 200
    def get(self):  
        count = 0
        data = []   

        while count < 100000:
            current_time = str(int(time.time())) 
            count += 1

            positive_count = random.randint(1, 100)
            negative_count = 100 - positive_count
            
            data.append({
                "date": current_time,
                "positive": str(positive_count),
                "negative": str(negative_count)
            })
        with open('data.json', 'w') as file:  
            json.dump(data, file)

        with open('data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)

registr_post = reqparse.RequestParser()
registr_post.add_argument("name", type=str, help="Task is email", required = True)
registr_post.add_argument("password", type=str, help="Task is email", required = True)

class Registration(Resource):
    def post(self):
        args = registr_post.parse_args()
        count = User.query.filter_by(email=args["name"]).count()
        if args["name"] and args['password'] and count==0:
            item = User(email = args["name"], password_hash = args['password'])
            db.session.add(item)
            db.session.commit()
            return jsonify({"registr" : "true"})
        return  jsonify({"registr" : "false"})

class Authentication(Resource):
    def post(self):
        args = registr_post.parse_args()
        item = User.query.filter_by(email=args["name"], password_hash = args['password']).first()
        print(item)
        if item: 
            return jsonify({"auth" : "true"})
        return jsonify({"auth" : "false"})

class Download(Resource):
    def post(self):
        files = request.get_json()
        print(files)
        return {'message': 'Received the data successfully'}, 200