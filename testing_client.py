from unittest import TestCase as _TestCase
from app import app as flask_app

from injector import Binder
from flask_injector import FlaskInjector

from providers.store_provider import StoreProvider
from fixtures.test_data import test_orders, test_status

class TestCase(_TestCase):
  @classmethod
  def setUpClass(cls):
    cls.test_orders = test_orders
    cls.test_status = test_status

  def setUp(self):
    app = flask_app.app
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['DEBUG'] = False
    self.app = app.test_client()

    self.store_provider = StoreProvider(self.test_orders, self.test_status) 

    def configure_test_bindings(binder):
      binder.bind(
        StoreProvider,
        to=self.store_provider,
      )

      return binder

    FlaskInjector(app=app, modules=[configure_test_bindings])



