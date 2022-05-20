import os

host = os.environ.get('API_HOST')
key = os.environ.get('API_KEY')

headers = {
    'x-rapidapi-host': host,
    'x-rapidapi-key': key
    }