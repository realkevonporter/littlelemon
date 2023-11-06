from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class  MenuViewTest(TestCase):
    def setUp(self):
        
        MenuItem.objects.create(title="IceCream", price=10, inventory=3)
        MenuItem.objects.create(title="Weed", price=30, inventory=15)
        MenuItem.objects.create(title="Rum", price=25, inventory=4)
        #self.menuitem = MenuItemSerializer(data={"title":"Weed","price": 30, "inventory":100})
        #self.menuitem.is_valid()
    def test_getall(self):
        
        item = MenuItem.objects.all()
        serialized = MenuItemSerializer(item, many=True)
        
        self.assertEqual(serialized.data, MenuItemSerializer(MenuItem.objects.all(), many=True).data)
    
