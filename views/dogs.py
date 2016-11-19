# encoding: utf-8
from flask import jsonify, request
from flask.views import MethodView
from project.app import db
from project.models import Dog


class DogAPI(MethodView):
    def get(self, id):
        if id is None:
            d = Dog.query.all()
        else:
            d = Dog.query.get(id)
        return jsonify(d)

    def post(self):
        dog = Dog(
            name=request.form.get('name'),
            size=request.form.get('size'),
            born_date=request.form.get('born_date')
        )
        db.session.add(dog)
        db.session.commit()
        return jsonify({'message': 'Dog created successfully.'})

    def put(self, id):
        pass

    def delete(self, id):
        pass
