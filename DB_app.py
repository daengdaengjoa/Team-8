from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)


class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, nullable=False)
    pw = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    area = db.Column(db.String, nullable=False)


class Posting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    movie_title = db.Column(db.String, nullable=False)
    posting_title = db.Column(db.String, nullable=False)
    review = db.Column(db.String, nullable=False)
    grade = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, nullable=False)
    detail = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    
class Crawling(db.Model):  # 크롤링 정보 데이터
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    info = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    star = db.Column(db.String, nullable=False)
    nums = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    title_user = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()
