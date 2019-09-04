from unittest import mock
from .testing_client import TestCase
from api.store import store_objs, orders


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

  @mock.patch('api.store.get_all_orders')
  def test_get_order_by_id_success(self, mock_get_all_orders):
    test_order = {
      "id": 1,
      "petId": 0,
      "quantity": 0,
      "shipDate": "2019-09-04T11:37:27.985Z",
      "status": "placed",
      "complete": False,
    }

    mock_get_all_orders.return_value = [test_order]
    response = self.app.get('/store/order/1', follow_redirects=True) 

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json, test_order)

  @mock.patch('api.store.get_all_orders')
  def test_get_order_by_id_no_order(self, mock_get_all_orders):
    mock_get_all_orders.return_value = []
    response = self.app.get('/store/order/4', follow_redirects=True)

    self.assertEqual(response.status_code, 404)

