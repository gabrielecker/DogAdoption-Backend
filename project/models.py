# encoding: utf-8
from flask_login import UserMixin
from project.app import bcrypt, db, login_serializer


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    phone = db.Column(db.String)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, email, phone=None, password=None):
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password

    def __repr__(self):
        return u'<User %s>' % self.username

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def get_auth_token(self):
        data = [str(self.id), (self.username, self.password)]
        return login_serializer.dumps(data)


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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User, backref='dogs')
    photo = db.Column(db.Unicode)
    size = db.Column(db.String)
    born_date = db.Column(db.Date)
    location = db.Column(db.String)

    def __init__(
        self, name, description=None, size=None, photo=None,
        born_date=None, breed_id=None, location=None, user_id=None
    ):
        self.name = name
        self.description = description
        self.size = size
        self.photo = photo
        self.born_date = born_date
        self.breed_id = breed_id
        self.location = location
        self.user_id = user_id

    def __repr__(self):
        return u'<Dog %s>' % self.name
