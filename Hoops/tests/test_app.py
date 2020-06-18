import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db, bcrypt
from application.models import Users, Comments, Players
from os import getenv

class TestBase(TestCase):

    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_URI'),
                SECRET_KEY=getenv('TEST_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

        hashed_pw = bcrypt.generate_password_hash('test')
        test_1 = Users(first_name='test', last_name='sub', email='test@test.com', password=hashed_pw)

        hashed_pw2 = bcrypt.generate_password_hash('test2')
        test_2 = Users(first_name='new', last_name='test', email='new@test.com', password=hashed_pw2)

        
        db.session.add(test_1)
        db.session.add(test_2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

class TestComments(TestBase):
    
    def test_add_new_comment(self):
        with self.client:
            self.client.post(
                    '/login',
                    data=dict(
                        email='test@test.com',
                        password='test'),
                    )
            response = self.client.post(
                    '/comment',
                    data=dict(
                        title='Test Title',
                        content='Test Content',
                        player='New Player'
                    ),
                    follow_redirects=True
                )
            self.assertIn(b'New Player', response.data)

class TestUpdate(TestBase):

    def test_update_comment(self):
        with self.client:
            self.client.post(
                    '/login',
                    data=dict(
                        email='test@test.com',
                        password='test'),
                    )
            self.client.post(
                    '/comment',
                    data=dict(
                        title='Test Title',
                        content='Test Content',
                        player='New Player'
                    ),
                )
            response = self.client.post(
                    '/update',
                    data=dict(
                        comment_id= 1,
                        title="New Title",
                        content="New",
                        player="New Player"),
                    follow_redirects=True
                    )
            self.assertIn(b'New Title', response.data)

class TestDelete(TestBase):

    def test_delete_comment(self):
        with self.client:
            self.client.post(
                    '/login',
                    data=dict(
                        email='test@test.com',
                        password='test'),
                    )
            self.client.post(
                    '/comment',
                    data=dict(
                        title='Test Title',
                        content='Test Content',
                        player='New Player'
                    ),
                )
            response = self.client.post(
                    '/delete',
                    data=dict(
                        comment_id=1),
                    follow_redirects=True)
            self.assertIn(b'', response.data)

class TestRegister(TestBase):

    def test_regpage(self):
            response = self.client.get(url_for('register'))
            self.assertEqual(response.status_code, 200)


class TestPlayer(TestBase):

    def test_player_creation(self):
        with self.client:
            self.client.post(
                    '/login',
                    data=dict(
                        email='test@test.com',
                        password='test'),
                    )
            self.client.post(
                    '/comment',
                    data=dict(
                        title='Test Title',
                        content='Test Content',
                        player='New Player'
                    ),
                )
            response = self.client.get(url_for('players'))
            self.assertIn(b'New Player', response.data)
