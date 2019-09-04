

class StoreProvider(object):
  def __init__(self, orders, status):
    self.orders = orders
    self.status = status

  def get_all_orders(self):
    return self.orders

  def find_order_by_id(self, order_id):
    for order in self.get_all_orders():
      if (order['id'] == order_id):
        return order

    return None

  def add_order(self, order):
    self.orders.append(order)

  def get_status(self):
    return self.status

  def get_orders(self):
    return self.orders