from unittest import TestCase as _TestCase
from app import app as flask_app



class TestCase(_TestCase):

  def setUp(self):
    app = flask_app.app
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['DEBUG'] = False
    self.app = app.test_client()




