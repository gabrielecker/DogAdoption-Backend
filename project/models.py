# encoding: utf-8
from project.app import db


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
    breed = db.relationship('Breed', backref='dogs')
    size = db.Column(db.String)
    born_date = db.Column(db.DateTime)

    def __init__(self, name, size, born_date):
        self.name = name
        self.size = size
        self.born_date = born_date

    def __repr__(self):
        return u'<Dog %s>' % self.name
