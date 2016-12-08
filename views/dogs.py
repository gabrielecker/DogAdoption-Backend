# encoding: utf-8
from flask import jsonify, request
from flask_login import login_required
from project.app import db
from project.models import Dog
from utils.rest import RestView


class DogAPI(RestView):
    schema = 'Dog'

    @login_required
    def get(self, id):
        if id is None:
            dogs = Dog.query.all()
            return jsonify(self.list_parser.dump(dogs).data)
        else:
            dog = Dog.query.get(id)
            return jsonify(self.parser.dump(dog).data)

    @login_required
    def post(self):
        data = request.get_json()
        dog = Dog(**data)
        db.session.add(dog)
        db.session.commit()
        return self.make_response('Dog created successfully.', 201)

    @login_required
    def put(self, id):
        data = request.get_json()
        Dog.query.filter_by(id=id).update(data)
        db.session.commit()
        return self.make_response('Dog updated successfully.')

    @login_required
    def delete(self, id):
        dog = Dog.query.get(id)
        db.session.delete(dog)
        db.session.commit()
        return self.make_response('Dog deleted successfully.')
