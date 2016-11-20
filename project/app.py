# encoding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('project.config')
db = SQLAlchemy(app)

# Import APIs after SQLAlchemy otherwise it's a circular import.
from views.dogs import DogAPI

dog_view = DogAPI.as_view('dog_api')
app.add_url_rule('/dogs/', defaults={'id': None},
                 view_func=dog_view, methods=['GET'])
app.add_url_rule('/dogs/', view_func=dog_view, methods=['POST'])
app.add_url_rule('/dogs/<int:id>', view_func=dog_view,
                 methods=['GET', 'PUT', 'DELETE'])
