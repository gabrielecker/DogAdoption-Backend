# encoding: utf-8
from flask import jsonify, request
from flask.views import MethodView
from project.app import db
from project.models import Dog
from utils.schemas import SchemaFactory


class DogAPI(MethodView):
    def get(self, id):
        if id is None:
            dogs = Dog.query.all()
            parser = SchemaFactory.get_schema('Dog', True)
            return jsonify(parser.dump(dogs).data)
        else:
            dog = Dog.query.get(id)
            parser = SchemaFactory.get_schema('Dog')
            return jsonify(parser.dump(dog).data)

    def post(self):
        data = request.get_json()
        dog = Dog(**data)
        db.session.add(dog)
        db.session.commit()
        return jsonify({'message': 'Dog created successfully.'})

    def put(self, id):
        data = request.get_json()
        Dog.query.filter_by(id=id).update(data)
        db.session.commit()
        return jsonify({'message': 'Dog updated successfully.'})

    def delete(self, id):
        dog = Dog.query.get(id)
        db.session.delete(dog)
        db.session.commit()
        return jsonify({'message': 'Dog deleted successfully.'})
