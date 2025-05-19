from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setup(self):
        self.item1 = MenuItem.objects.create(title="Pizza", price=12.5, inventory=30)
        self.item2 = MenuItem.objects.create(title="IceCream", price=7.9, inventory=40)
        self.client = APIClient()

    def test_getall(self):
        response = self.client.get("/restaurant/menu/")
        serialize_data = MenuSerializer(MenuItem.objects.all(), many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serialize_data)


