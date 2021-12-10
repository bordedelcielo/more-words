from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import requests
from datetime import datetime
import json
from flask_login import UserMixin, LoginManager
import uuid
import secrets
from werkzeug.security import generate_password_hash

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    username = db.Column(db.String(150), nullable = False, default='')
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, username, id='',password='',token='',g_auth_verify=False):
        self.id = self.set_id()
        self.username = username
        self.password = self.set_password(password)
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    

# class Word(db.Model):
#     word = db.Column(db.String(150), primary_key = True)
#     definition = db.Column(db.String(500))
#     date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

#     def __init__(self, word):
#         self.word = "panettone"
#         self.definition = (requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")).json()[0]["meanings"][0]["definitions"][0]["definition"]