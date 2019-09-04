from .testing_client import TestCase
from api.store import store_objs


class StoreAPITestCase(TestCase):
  def test_get_store_inventory_success(self):
    response = self.app.get('/store/inventory/')

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json, store_objs)

