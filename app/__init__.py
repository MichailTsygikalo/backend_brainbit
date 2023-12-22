from flask_restful import Api
from flask import Flask
app=Flask(__name__)
api = Api(app)
from app import route

if __name__ == "__name__":
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)

