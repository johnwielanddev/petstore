from .testing_client import TestCase
from api.store import store_objs


class StoreAPITestCase(TestCase):
  def test_get_store_inventory_success(self):
    response = self.app.get('/store/inventory/')

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json, store_objs)

  def test_order_success(self):
    new_order = {
      "id": 0,
      "petId": 0,
      "quantity": 0,
      "shipDate": "2019-09-04T11:37:27.985Z",
      "status": "placed",
      "complete": False,
    }

    response = self.app.post('/store/order', json=new_order, 
                             follow_redirects=True)

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json, new_order)

  def test_failed_order_invalid_id(self):
    new_order = {
      "id": "0",
      "petId": 0,
      "quantity": 0,
      "shipDate": "2019-09-04T11:37:27.985Z",
      "status": "placed",
      "complete": False,
    }

    response = self.app.post('/store/order', json=new_order,
                             follow_redirects=True)

    self.assertEqual(response.status_code, 400)



