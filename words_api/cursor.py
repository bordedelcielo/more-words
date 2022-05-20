import psycopg2
import os

database = os.environ.get('DATABASE')
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
port = os.environ.get('DB_PORT')

con = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)