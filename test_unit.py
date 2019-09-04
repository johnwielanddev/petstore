from unittest import TestCase

from api.store import get, store_objs

class StoreInventoryTest(TestCase):
  def test_get_store_inventory(self):
    self.assertEqual(get(), store_objs)



