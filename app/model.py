from app import db


    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(256))

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Integer, nullable=False)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_survey = db.Column(db.Integer, db.ForeignKey('survey.id'))
    positive = db.Column(db.Integer, nullable=False)
    negative = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(50), nullable=False)


