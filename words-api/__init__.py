from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from config import Config
from .models import db as root_db
from .helpers import JSONEncoder
from .site.routes import site

app = Flask (__name__)

app.register_blueprint(site)

app.config.from_object(Config)

migrate = Migrate(app, root_db)

app.json_encoder = JSONEncoder