# encoding: utf-8
from flask import jsonify, request
from flask_login import login_user, login_required, logout_user
from project.app import bcrypt, db, login_manager, login_serializer
from project.models import User
from sqlalchemy.exc import IntegrityError
from utils.rest import RestView


@login_manager.user_loader
def load_user(id):
    user = User.query.get(id)
    return user


@login_manager.request_loader
def load_token(request):
    token = request.headers.get('Authorization', None)
    if token is not None:
        try:
            data = login_serializer.loads(token)
        except:
            return None
        user = User.query.get(data[0])
        if user and user.password == data[1]:
            return user
    return None


class UserAPI(RestView):
    schema = 'User'

    def get(self, id):
        if id is None:
            users = User.query.all()
            return jsonify(self.list_parser.dump(users).data)
        else:
            user = User.query.get(id)
            return jsonify(self.parser.dump(user).data)

    def post(self):
        try:
            data = request.get_json()
            user = User(**data)
            user.set_password(user.password)
            db.session.add(user)
            db.session.commit()
            return self.make_response('User created successfully.', 201)
        except IntegrityError as error:
            return self.make_response(error.message, 400)

    @login_required
    def put(self, id):
        try:
            data = request.get_json()
            data['password'] = bcrypt.generate_password_hash(data['password'])
            User.query.filter_by(id=id).update(data)
            db.session.commit()
            return self.make_response('User updated successfully.')
        except IntegrityError as error:
            return self.make_response(error.message, 400)

    @login_required
    def delete(self, id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return self.make_response('User deleted successfully.')


class LoginAPI(RestView):

    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            login_user(user, remember=True)
            return self.make_response('Logged in successfully.')
        else:
            return self.make_response('Invalid username or password.', 400)


class LogoutAPI(RestView):

    @login_required
    def get(self, id):
        logout_user()
        return self.make_response('Logged out successfully.')
