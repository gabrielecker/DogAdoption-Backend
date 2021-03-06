# encoding: utf-8
from flask import jsonify, request
from flask_login import login_required
from project.app import db
from project.models import Breed
from utils.rest import RestView


class BreedAPI(RestView):
    schema = 'Breed'

    def get(self, id):
        if id is None:
            breeds = Breed.query.all()
            return jsonify(self.list_parser.dump(breeds).data)
        else:
            breed = Breed.query.get(id)
            return jsonify(self.parser.dump(breed).data)

    @login_required
    def post(self):
        data = request.get_json()
        breed = Breed(**data)
        db.session.add(breed)
        db.session.commit()
        return self.make_response('Breed created successfully.', 201)

    @login_required
    def put(self, id):
        data = request.get_json()
        Breed.query.filter_by(id=id).update(data)
        db.session.commit()
        return self.make_response('Breed updated successfully.')

    @login_required
    def delete(self, id):
        breed = Breed.query.get(id)
        if breed:
            db.session.delete(breed)
            db.session.commit()
            return self.make_response('Breed deleted successfully.')
        else:
            return self.make_response('Breed not found.', 404)


class BreedDogsAPI(RestView):
    schema = 'BreedDogs'

    def get(self, id):
        breed = Breed.query.get(id)
        return jsonify(self.parser.dump(breed).data)
