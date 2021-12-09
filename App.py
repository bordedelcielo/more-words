from flask import Flask, render_template
import requests
import json
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from flask_migrate import Migrate
from config import Config

app = Flask (__name__)

app.config.from_object(Config)
db = SQLAlchemy()
ma = Marshmallow()
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def Index ():
    word = "panettone"
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    data = response.json()[0]["meanings"][0]["definitions"][0]["definition"]
    # json_data = json.loads(data) # converts data to a Python object.
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)

class Word(db.Model):
    word = db.Column(db.String(150), primary_key = True)
    definition = db.Column(db.String(500))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, word):
        self.word = "panettone"
        self.definition = (requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")).json()[0]["meanings"][0]["definitions"][0]["definition"]