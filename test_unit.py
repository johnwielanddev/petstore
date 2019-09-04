from unittest import TestCase, mock

from api.store import get, store_objs, find_order_by_id, orders 

test_orders = [
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


class StoreInventoryTest(TestCase):
  def test_get_store_inventory(self):
    self.assertEqual(get(), store_objs)

  @mock.patch('api.store.get_orders')
  def test_find_order_by_id_success(self, mock_orders):
    mock_orders.return_value = test_orders

    self.assertEqual(find_order_by_id(3), test_orders[1])

  @mock.patch('api.store.get_orders')
  def test_find_order_by_id_fail(self, mock_orders):
    mock_orders.return_value = test_orders

    self.assertEqual(find_order_by_id(55), None)



