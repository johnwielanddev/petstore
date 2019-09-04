

store_objs = {
  "a_status": 0,
  "another_status": 10,
}

orders = []


def get():
  return store_objs 

def order(order):
  orders.append(order)
  return order


