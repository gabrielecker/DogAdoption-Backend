# encoding: utf-8
from project.app import app, db
from project.models import Breed, Dog, User
from flask_testing import TestCase
import unittest


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('project.config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        breed = Breed(name='test')
        dog = Dog(name='test')
        user = User(username='test', email='test@test.com')
        user.set_password('test')
        db.session.add(breed)
        db.session.add(dog)
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class BreedTestCase(BaseTestCase):

    def test_breeds_get(self):
        response = self.client.get('/breeds/')
        self.assertEqual(response.status_code, 200)

    def test_breeds_post_unauthorized(self):
        data = {'name': 'Chihuahua'}
        response = self.client.post('/breeds/', data=data)
        self.assertEqual(response.status_code, 401)

    def test_breeds_post_authorized(self):
        response = self.client.post(
            '/login/',
            data={'username': 'test', 'password': 'test'}
        )
        self.assertEqual(response.status_code, 200)

        data = {'name': 'Chihuahua'}
        response = self.client.post('/breeds/', data=data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
