# encoding: utf-8
from flask import abort, jsonify
from flask.views import MethodView
from utils.schemas import SchemaCreator


class RestView(MethodView):

    def __init__(self):
        if hasattr(self, 'schema') and self.schema is not None:
            self.parser, self.list_parser = SchemaCreator.get_schemas(
                self.schema
            )

    def __doc__(self):
        return 'Basic REST interface, returns 405 (method not allowed) \
in case you dont implement any of those and create schemas.'

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


class Router(object):

    def __init__(self, app):
        self.app = app

    def __doc__(self):
        return 'Router which allows declaring urls django stylish and \
registering in the app with REST structure. Takes the app as a parameter.'

    def register_views(self, urls):
        for url in urls:
            self.app.add_url_rule(
                url[0], defaults={'id': None},
                view_func=url[1], methods=['GET']
            )
            self.app.add_url_rule(
                '%s<int:id>/' % url[0], view_func=url[1],
                methods=['GET', 'PUT', 'DELETE']
            )
            self.app.add_url_rule(url[0], view_func=url[1], methods=['POST'])
