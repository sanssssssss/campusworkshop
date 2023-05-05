"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaacs67avj5o48lkhvg-a.oregon-postgres.render.com",
        database="todo_u46h",
        user="root",
        password="5XbmbIn2oZloUZGLZ2J4IW4xsf0ODLlG")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
