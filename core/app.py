from flask import Flask
from flask import g
from core.config import runtime_config

import sqlite3
import os

from core.routes.cipher import Cipher


DATABASE = os.environ.get('DATABASE', '/core/models/database.db')

app = Flask(__name__)
app.config.from_object(runtime_config())


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    return Cipher().main_page()
