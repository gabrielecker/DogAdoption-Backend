#!/usr/bin/env python
# encoding: utf-8
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from project.app import app, db
from project.models import User, Breed, Dog
import json

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


def bulk_insert(file, model):
    with open(file) as j:
        data = json.loads(j.read())
        db.session.bulk_save_objects([model(**breed) for breed in data])


@manager.command
def load_data():
    bulk_insert('fixtures/breeds.json', Breed)
    bulk_insert('fixtures/users.json', User)
    bulk_insert('fixtures/dogs.json', Dog)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
