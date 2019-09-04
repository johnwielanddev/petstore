from unittest import TestCase as _TestCase
from app import app as flask_app

from injector import Binder
from flask_injector import FlaskInjector

from providers.store_provider import StoreProvider

test_orders = [
  {
    "id": 1,
    "petId": 0,
    "quantity": 0,
    "shipDate": "2019-09-04T11:37:27.985Z",
    "status": "placed",
    "complete": False,
  },
  {
    "id": 0,
    "petId": 0,
    "quantity": 0,
    "shipDate": "2019-09-04T11:37:27.985Z",
    "status": "placed",
    "complete": False,
  },
  {
    "id": 3,
    "petId": 0,
    "quantity": 0,
    "shipDate": "2019-09-04T11:37:27.985Z",
    "status": "placed",
    "complete": False,
  },
  {
    "id": 99,
    "petId": 0,
    "quantity": 0,
    "shipDate": "2019-09-04T11:37:27.985Z",
    "status": "placed",
    "complete": False,
  },
]

test_status = {
  'OK': 0,
  "VACCINATED": 0,
  "DEAD": 0,
  "CAT": 0
}


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



