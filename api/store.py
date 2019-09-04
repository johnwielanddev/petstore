

store_objs = {
  "a_status": 0,
  "another_status": 10,
}

orders = []


def get():
  return store_objs 

def get_order(order):
  orders.append(order)
  return order

def get_all_orders():
  return orders

def find_order_by_id(order_id):
  for order in get_all_orders():
    if (order['id'] == order_id):
      return order

  return None


def get_order_by_id(order_id):
  order = find_order_by_id(order_id)
  if order:
    return order, 200

  return None, 404 


