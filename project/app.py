# encoding: utf-8
from decouple import config
from flask import Flask, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer
from utils.rest import Router


app = Flask(__name__)
app.config.from_object(config('APP_CONFIG'))
CORS(app, supports_credentials=True)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
router = Router(app)


# TODO: Make it look better
@app.errorhandler(400)
@app.errorhandler(401)
def error_handler(e):
    return jsonify({'message': e.description}), e.code

# Urls imported after db to avoid circular import problems.
from project.urls import urls # NOQA

router.register_views(urls)
