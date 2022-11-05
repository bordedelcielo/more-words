# MORE WORDS

A Flask website for managing word definitions.

Hosted on Glitch here: https://cream-dust-beanie.glitch.me/

## Local Install

1. Use `env` for the name of your venv folder.
2. Register for the [Lingua Robot](https://rapidapi.com/rokish/api/lingua-robot/) API and set the values for `X-RapidAPI-Key` and `X-RapidAPI-Host` for environment variables `API_KEY` and `API_HOST`, respectively.
3. Set the environment variable `FLASK_APP=words_api`.
4. By default it will use an SQLite database at `app.db`. If you want to use postgres, set the environment variable `SQLALCHEMY_DATABSE_URI=postgresql://your_db`.
5. `flask db init`
6. `flask db migrate -m "Initial migration"`
7. `flask db upgrade`
8. `flask run`
