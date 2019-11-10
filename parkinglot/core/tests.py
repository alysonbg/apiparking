from rest_framework.test import APITestCase
from rest_framework import serializers

class TestParking(APITestCase):
    def test_create_parking(self):
        """Testa se o parking é criado quando uma requisicao POST ao endpoing /parking"""
        response = self.client.post('/parking/', {'plate': 'AAA-9999'})
        self.assertEqual({'id': 1}, response.data)

        
