# encoding: utf-8
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from functools import partial
from utils.rest import register_views

app = Flask(__name__)
app.config.from_object('project.config')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)

# Urls imported after db to avoid circular import problems.
from project.urls import urls # NOQA

app.register_views = partial(register_views, app)
app.register_views(urls)
