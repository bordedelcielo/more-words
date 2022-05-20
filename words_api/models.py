from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import requests
from datetime import datetime
import json
from flask_login import UserMixin, LoginManager
import uuid
import words_api.headers as headers
from werkzeug.security import generate_password_hash

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    email = db.Column(db.String(150), nullable = False)
    username = db.Column(db.String(150), nullable = False, default='')
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, username, id='',password='',token='',g_auth_verify=False):
        self.id = self.set_id()
        self.email = email
        self.username = username
        self.password = self.set_password(password)
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return headers.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    

class Word(db.Model):
    id = db.Column(db.String, primary_key = True)
    word = db.Column(db.String(150))
    definition = db.Column(db.String(500))
    status = db.Column(db.String(50))
    added_by_user = db.Column(db.String(150), nullable = False, default='')
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    # user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, word, definition, added_by_user, status='', id=''):
        self.id = self.set_id()
        self.word = word
        self.definition = definition
        self.status = status
        self.added_by_user = added_by_user

    def __repr__(self):
        return f'The following Word has been added: {self.word}, {self.definition}'

    def set_id(self):
        return (headers.token_urlsafe())

class WordSchema(ma.Schema):
    class Meta:
        fields = ['id', 'word', 'definition']

word_schema = WordSchema()
words_schema = WordSchema(many = True)

# random change