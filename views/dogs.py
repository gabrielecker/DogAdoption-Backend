# encoding: utf-8
from flask import jsonify, request
from flask_login import login_required, current_user
from project.app import db
from project.models import Dog
from utils.rest import RestView


class DogAPI(RestView):
    schema = 'Dog'

    def get(self, id):
        page = request.args.get('page') or 1
        if id is None:
            dogs = Dog.query.paginate(page=int(page), per_page=6)
            return jsonify({
                'items': self.list_parser.dump(dogs.items).data,
                'page': dogs.page,
                'total': dogs.total
            })
        else:
            dog = Dog.query.get(id)
            return jsonify(self.parser.dump(dog).data)

    @login_required
    def post(self):
        data = request.get_json()
        dog = Dog(**data)
        dog.user = current_user
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
        if dog:
            db.session.delete(dog)
            db.session.commit()
            return self.make_response('Dog deleted successfully.')
        else:
            return self.make_response('Dog not found.', 404)


class UserDogsAPI(RestView):
    schema = 'Dog'

    @login_required
    def get(self, id):
        dogs = Dog.query.filter_by(user=current_user)
        return jsonify(self.list_parser.dump(dogs).data)
