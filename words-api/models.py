from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import requests
from datetime import datetime
import json
from flask_login import UserMixin, LoginManager
import uuid
import secrets

db = SQLAlchemy()
# login_manager = LoginManager()
# ma = Marshmallow()

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

# class User(db.Model, UserMixin):
    

# class Word(db.Model):
#     word = db.Column(db.String(150), primary_key = True)
#     definition = db.Column(db.String(500))
#     date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

#     def __init__(self, word):
#         self.word = "panettone"
#         self.definition = (requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")).json()[0]["meanings"][0]["definitions"][0]["definition"]