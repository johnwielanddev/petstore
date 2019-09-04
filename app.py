import connexion
from connexion.resolver import RestyResolver


if __name__ == '__main__':
  app = connexion.App(__name__, port=9090, specification_dir='swagger/')
  app.add_api('petstore.yml', resolver=RestyResolver('api'))
  app.run()
