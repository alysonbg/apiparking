from rest_framework.test import APITestCase
from rest_framework import serializers

class TestParking(APITestCase):
    def test_create_parking(self):
        """Testa se o parking é criado quando uma requisicao POST ao endpoing /parking"""
        response = self.client.post('/parking/', {'plate': 'AAA-9999'})
        self.assertEqual({'id': 1}, response.data)

    def test_return_parking_history(self):
        """Testa se retorna o histórico de estacionamentos de um carro"""
        self.client.post('/parking/', {'plate': 'BBB-8888'})
        response = self.client.get('/parking/BBB-8888/')
        self.assertIsInstance(response.data, list)

        
