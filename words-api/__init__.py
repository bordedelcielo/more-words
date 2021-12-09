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

# Insert blueprints here.

app.config.from_object(Config)

# root_db.init_app(app)

migrate = Migrate(app, root_db)

# login_manager.init_app(app)
# login_manager.login_view = 'auth.signin'

# ma.init_app(app)

app.json_encoder = JSONEncoder