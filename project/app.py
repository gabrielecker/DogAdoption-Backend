# encoding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils.rest import register_views

app = Flask(__name__)
app.config.from_object('project.config')
db = SQLAlchemy(app)

# Urls imported after db to avoid circular import problems.
from project.urls import urls # NOQA

register_views(app, urls)
