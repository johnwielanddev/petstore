import connexion

from injector import Binder
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver

from providers.store_provider import StoreProvider
from fixtures.test_data import test_orders, test_status


def configure_bindings(binder):
  binder.bind(
    StoreProvider,
    to=StoreProvider(test_orders, test_status)
  )

  return binder


app = connexion.App(__name__, port=9090, specification_dir='swagger/')
app.add_api('petstore.yml', resolver=RestyResolver('api'))

if __name__ == '__main__':
  FlaskInjector(app=app.app, modules=[configure_bindings])
  app.run()

