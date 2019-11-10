from rest_framework.test import APITestCase


class TestParking(APITestCase):
    def test_create_parking(self):
        """Testa se o parking é criado quando uma requisicao POST ao endpoing /parking"""
        response = self.client.post('/parking/', {'plate': 'AA-9999'})
        self.assertEqual({'id': 1}, response.data)
