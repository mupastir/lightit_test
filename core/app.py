from flask import Flask
from flask import g
from core.config import runtime_config

import os

from core.routes.cipher import CipherRoute


DATABASE = os.environ.get('DATABASE', '/core/models/database.db')

app = Flask(__name__)
app.config.from_object(runtime_config())


@app.route('/')
def index():
    return CipherRoute().main_page()


@app.route('/cipher', methods=['POST'])
def cipher():
    return CipherRoute().cipher()
