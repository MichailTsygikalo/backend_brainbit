from app import app, api
from flask_restful import Resource, fields, marshal_with, abort,reqparse
from flask import render_template
from app.logic import ResponceTest, Registration, Authentication, Download
import json
import random
@app.route('/test', methods = [ 'GET'])
def test():
    return render_template("index.html")

@app.route('/', methods = [ 'GET'])
def index():
    json_data = []
    # Generating 100 data points
    for _ in range(1000):
        data_point = {
            "date": str((1500000000+_)),  # Random timestamp between 2017 and 2027
            "positive": str(random.randint(0, 100)),
            "negative": str(random.randint(0, 100)),
        }
        json_data.append(data_point)

    processed_data = []
    for item in json_data:
        date = int(item['date'])
        positive = int(item['positive'])
        negative = int(item['negative'])
        processed_data.append({'x': date, 'y': positive})
        
    return render_template('index.html', data=json.dumps(processed_data))

api.add_resource(ResponceTest, '/test')
api.add_resource(Registration, '/registr')
api.add_resource(Authentication, '/auth')
api.add_resource(Download, '/dwn')
