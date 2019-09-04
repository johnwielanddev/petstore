from unittest import TestCase, mock, skip

from api.store import get, post_order, get_order_by_id, delete_order_by_id
from providers.store_provider import StoreProvider

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

test_status = {
  'OK': 0,
  "VACCINATED": 0,
  "DEAD": 0,
  "CAT": 0
}

class StoreAPITest(TestCase):
  def test_get_store_inventory(self):
    store_provider = StoreProvider({}, test_status)

    self.assertEqual(get(store_provider), test_status)
  
  def test_get_order_by_id_order_not_found(self):
    store_provider = StoreProvider(test_orders, {})

    self.assertEqual(get_order_by_id(store_provider, 1), (None, 404))


class StoreProviderTest(TestCase):
  def test_find_order_by_id_success(self):
    store_provider = StoreProvider(test_orders, {})

    self.assertEqual(store_provider.find_order_by_id(3), test_orders[1])

  def test_find_order_by_id_fail(self):
    store_provider = StoreProvider(test_orders, {})
    
    self.assertEqual(store_provider.find_order_by_id(55), None)

  @skip
  @mock.patch('api.store.get_all_orders')
  def test_delete_order_by_id_successful(self):
    mock_get_all_orders.return_value = test_orders
    self.assertEqual(delete_order_by_id(0), (None, 202))


