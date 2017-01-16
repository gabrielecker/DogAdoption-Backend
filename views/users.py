# encoding: utf-8
from flask import jsonify, request
from flask_login import login_required, logout_user
from project.app import app, bcrypt, db, login_manager, login_serializer
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
    max_age = app.config['REMEMBER_COOKIE_DURATION'].total_seconds()
    if token is not None:
        try:
            data = login_serializer.loads(token.split()[1], max_age=max_age)
            user = User.query.get(data[0])
            if user and [user.username, user.password] == data[1]:
                return user
        except:
            return None
    return None


class UserAPI(RestView):
    schema = 'User'

    @login_required
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
            return jsonify({'token': 'Bearer ' + user.get_auth_token()})
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
            return jsonify({
                'username': user.username,
                'token': 'Bearer ' + user.get_auth_token()
            })
        else:
            return self.make_response('Invalid username or password.', 401)


class LogoutAPI(RestView):

    @login_required
    def get(self, id):
        logout_user()
        return self.make_response('Logged out successfully.')
