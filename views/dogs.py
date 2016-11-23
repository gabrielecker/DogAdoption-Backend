# encoding: utf-8
from flask import jsonify, request
from project.app import db
from project.models import Dog
from utils.rest import RestView


class DogAPI(RestView):
    schema = 'Dog'

    def get(self, id):
        if id is None:
            dogs = Dog.query.all()
            return jsonify(self.list_parser.dump(dogs).data)
        else:
            dog = Dog.query.get(id)
            return jsonify(self.parser.dump(dog).data)

    def post(self):
        data = request.get_json()
        dog = Dog(**data)
        db.session.add(dog)
        db.session.commit()
        return self.make_response('Dog created successfully.')

    def put(self, id):
        data = request.get_json()
        Dog.query.filter_by(id=id).update(data)
        db.session.commit()
        return self.make_response('Dog updated successfully.')

    def delete(self, id):
        dog = Dog.query.get(id)
        db.session.delete(dog)
        db.session.commit()
        return self.make_response('Dog deleted successfully.')
