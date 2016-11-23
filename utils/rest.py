# encoding: utf-8
from flask import abort, jsonify
from flask.views import MethodView
from utils.schemas import SchemaCreator


class RestView(MethodView):
    """
    Basic REST interface, returns 405 (method not allowed)
    in case you don't implement any of those and create schemas.
    """
    def __init__(self):
        if hasattr(self, 'schema') and self.schema is not None:
            self.parser, self.list_parser = SchemaCreator.get_schemas(
                self.schema
            )

    def get(self, id):
        abort(405)

    def post(self):
        abort(405)

    def put(self, id):
        abort(405)

    def delete(self, id):
        abort(405)

    def make_response(self, content, status=200):
        return jsonify({'message': content}), status


def register_views(app, urls):
    for url in urls:
        app.add_url_rule(
            url[0], defaults={'id': None},
            view_func=url[1], methods=['GET']
        )
        app.add_url_rule(
            '%s<int:id>/' % url[0], view_func=url[1],
            methods=['GET', 'PUT', 'DELETE']
        )
        app.add_url_rule(url[0], view_func=url[1], methods=['POST'])
