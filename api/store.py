from flask_injector import inject
from providers.store_provider import StoreProvider

@inject
def get(store_provider: StoreProvider):
  return store_provider.get_status()

@inject
def post_order(store_provider: StoreProvider, order):
  store_provider.add_order(order)
  return order

@inject
def get_order_by_id(store_provider: StoreProvider, order_id):
  order = store_provider.find_order_by_id(order_id)
  if order:
    return order, 200

  return None, 404 

def delete_order_by_id(order_id):
  pass 
