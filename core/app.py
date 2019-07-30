from flask import Flask
from flask_redis import FlaskRedis

from core.config import runtime_config

from core.routes.cipher import Cipher


app = Flask(__name__)
app.config.from_object(runtime_config())


@app.route('/')
def index():
    return Cipher()


redis_client = FlaskRedis()
redis_client.init_app(app)
