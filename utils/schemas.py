# encoding: utf-8
from importlib import import_module
from marshmallow import Schema, fields


class UserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str()


class BreedSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class DogSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    breed = fields.Nested(BreedSchema)
    user = fields.Nested(UserSchema)
    photo = fields.Str()
    size = fields.Str()
    born_date = fields.Date()
    location = fields.Str()


class BreedDogsSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    dogs = fields.List(fields.Nested(DogSchema))


class SchemaCreator:
    @staticmethod
    def get_schemas(cls):
        try:
            Class = getattr(import_module('utils.schemas'), '%sSchema' % cls)
            return (Class(), Class(many=True))
        except:
            raise Exception('Error: Class %sSchema does not exist.' % cls)
