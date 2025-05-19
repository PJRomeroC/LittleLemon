from django.test import TestCase
from restaurant.models import MenuItem

class MenuTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=7.9, inventory = 100)
        self.assertEqual(str(item), "IceCream : 7.9")