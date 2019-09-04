from unittest import TestCase, mock, skip

from fixtures.test_data import test_orders, test_status
from api.store import get, post_order, get_order_by_id, delete_order_by_id
from providers.store_provider import StoreProvider


class StoreAPITest(TestCase):
  def test_get_store_inventory(self):
    store_provider = StoreProvider({}, test_status)

    self.assertEqual(get(store_provider), test_status)
  
  def test_get_order_by_id_order_not_found(self):
    store_provider = StoreProvider(test_orders, {})

    self.assertEqual(get_order_by_id(store_provider, 5), (None, 404))


class StoreProviderTest(TestCase):
  def test_find_order_by_id_success(self):
    store_provider = StoreProvider(test_orders, {})

    self.assertEqual(store_provider.find_order_by_id(3), test_orders[2])

  def test_find_order_by_id_fail(self):
    store_provider = StoreProvider(test_orders, {})
    
    self.assertEqual(store_provider.find_order_by_id(55), None)

  def test_delete_order_by_id_successful(self):
    order_to_delete = test_orders[0]
    store_provider = StoreProvider(test_orders, {})
    store_provider.delete_order_by_id(1)

    self.assertNotIn(order_to_delete, store_provider.orders)

  def test_delete_order_not_found(self):
    store_provider = StoreProvider(test_orders, {})

    res = store_provider.delete_order_by_id(9)
    self.assertEqual(res, False)

