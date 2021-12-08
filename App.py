from flask import Flask, render_template
import requests
import json

app = Flask (__name__)

@app.route('/')
def Index ():
    word = "panettone"
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    data = response.json()[0]["meanings"][0]["definitions"][0]["definition"]
    # json_data = json.loads(data) # converts data to a Python object.
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)

