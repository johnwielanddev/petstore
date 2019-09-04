from .testing_client import TestCase


class StoreAPITestCase(TestCase):


  def test_get_store_inventory_success(self):
    response = self.app.get('/store/inventory/')

    self.assertEquals(response.status_code, 200)


