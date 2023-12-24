from app import app, api
from flask_restful import Resource, fields, marshal_with, abort,reqparse
from flask import render_template, redirect, url_for, jsonify
from app.logic import ResponceTest, Registration, Authentication, Download,  DownloadTest, Upload, UploadRelax
from app.model import Data, User
from app.form import LoginForm
import json
import random
from flask_login import current_user, login_user, logout_user
from flask import g
@app.route('/test', methods = [ 'GET'])
def test():
    print(current_user.get_id())
    return render_template("index.html", user_id = current_user.get_id())

@app.route('/', methods = [ 'GET'])
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if current_user.is_authenticated:
        json_data = []
    # for _ in range(1000):
    #     data_point = {
    #         "date": str((1500000000+_)),  # Random timestamp between 2017 and 2027
    #         "positive": str(random.randint(0, 100)),
    #         "negative": str(random.randint(0, 100)),
    #     }
    #     json_data.append(data_point)

    items = Data.query.filter_by(id_user = 1, id_survey =7).all()
    for i in items:
        data_point ={
            "date": i.date,
            "positive": i.positive,
            "negative": i.negative,
        }
        json_data.append(data_point)
    processed_data = []
    for item in json_data:
        date = int(item['date'])
        positive = int(item['positive'])
        negative = int(item['negative'])
        processed_data.append({'x': date, 'y': positive})
    print(processed_data)
    return render_template('index.html', data=json.dumps(processed_data))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: 
        return redirect(url_for('index')) 
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        user = User.query.filter_by(email = str(form.username.data)).first()
        print(user)
        if user:
            login_user(user)
            return redirect(url_for('index'))
        print('Invalid username or password')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



api.add_resource(ResponceTest, '/test')
api.add_resource(Registration, '/registr')
api.add_resource(Authentication, '/auth')
api.add_resource(Download, '/dwn')
api.add_resource(Upload, '/upl')
api.add_resource(UploadRelax, '/uplrelax')
api.add_resource(DownloadTest, '/dwntest')
