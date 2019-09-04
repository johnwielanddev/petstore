from unittest import mock, skip
from .testing_client import TestCase, test_orders, test_status


class StoreAPITestCase(TestCase):
  def test_get_store_inventory_success(self):
    response = self.app.get('/store/inventory/')

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json, test_status)

  def test_add_order_success(self):
    new_order = {
      "id": 99,
      "petId": 91,
      "quantity": 0,
      "shipDate": "2019-09-04T11:37:27.985Z",
      "status": "placed",
      "complete": False,
    }

    response = self.app.post('/store/order', json=new_order, 
                             follow_redirects=True)

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json, new_order)

  def test_add_order_fail_invalid_id(self):
    new_order = {
      "id": "99",
      "petId": 91,
      "quantity": 0,
      "shipDate": "2019-09-04T11:37:27.985Z",
      "status": "placed",
      "complete": False,
    }

    response = self.app.post('/store/order', json=new_order,
                             follow_redirects=True)

    self.assertEqual(response.status_code, 400)

  def test_get_order_by_id_success(self):
    response = self.app.get('/store/order/1', follow_redirects=True) 

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json, test_orders[0])

  def test_get_order_by_id_no_order(self):
    response = self.app.get('/store/order/4', follow_redirects=True)

    self.assertEqual(response.status_code, 404)

  @skip
  @mock.patch('api.store.get_all_orders')
  def test_delete_order_by_id(self, mock_get_all_orders):
    mock_get_all_orders.return_value = [test_order]

    response = self.app.delete('/store/order/1', follow_redirects=True)

    self.assertEqual(response.status_code, 200)

