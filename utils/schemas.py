# encoding: utf-8
from importlib import import_module
from marshmallow import Schema, fields


class BreedSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class DogSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    breed = fields.Nested(BreedSchema)
    size = fields.Str()
    born_date = fields.DateTime()


class SchemaFactory():
    @staticmethod
    def get_schema(cls, many=False):
        try:
            Class = getattr(import_module('utils.schemas'), '%sSchema' % cls)
            return Class(many=many)
        except:
            raise Exception('Error: Class %sSchema does not exist.' % cls)
