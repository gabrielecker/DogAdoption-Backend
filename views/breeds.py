# encoding: utf-8
from flask import jsonify, request
from flask.views import MethodView
from project.app import db
from project.models import Breed
from utils.schemas import SchemaCreator


class BreedAPI(MethodView):
    _parser, _list_parser = SchemaCreator.get_schemas('Breed')

    def get(self, id):
        if id is None:
            breeds = Breed.query.all()
            return jsonify(self._list_parser.dump(breeds).data)
        else:
            breed = Breed.query.get(id)
            return jsonify(self._parser.dump(breed).data)

    def post(self):
        data = request.get_json()
        breed = Breed(**data)
        db.session.add(breed)
        db.session.commit()
        return jsonify({'message': 'Breed created successfully.'})

    def put(self, id):
        data = request.get_json()
        Breed.query.filter_by(id=id).update(data)
        db.session.commit()
        return jsonify({'message': 'Breed updated successfully.'})

    def delete(self, id):
        breed = Breed.query.get(id)
        db.session.delete(breed)
        db.session.commit()
        return jsonify({'message': 'Breed deleted successfully.'})
