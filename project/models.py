# encoding: utf-8
from flask_login import UserMixin
from project.app import bcrypt, db


class Breed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return u'<Breed %s>' % self.name


class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    breed_id = db.Column(db.Integer, db.ForeignKey('breed.id'))
    breed = db.relationship(Breed, backref='dogs')
    size = db.Column(db.String)
    born_date = db.Column(db.DateTime)

    def __init__(self, name, description, size, born_date, breed_id):
        self.name = name
        self.description = description
        self.size = size
        self.born_date = born_date
        self.breed_id = breed_id

    def __repr__(self):
        return u'<Dog %s>' % self.name


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return u'<User %s>' % self.username

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
