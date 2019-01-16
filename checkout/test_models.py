from django.test import TestCase
from .models import Order, OrderLineItem
from products.models import Category, Product
from django.utils import timezone

# Create your tests here.
class TestCheckoutModels(TestCase):
    
    def test_Order_Model(self):
        current_date=timezone.now()
        order = Order(full_name="Katie Kelly", phone_number=22442244, country="Example Country", postcode="12ABC34", town_or_city="Example town or city", street_address_1="11 Example street", street_address_2="apartment 11", county="Example County", date=current_date)
        order.save()
        self.assertEqual(order.full_name, "Katie Kelly")
        self.assertEqual(order.phone_number, 22442244)
        self.assertEqual(order.country, "Example Country")
        self.assertEqual(order.postcode, "12ABC34")
        self.assertEqual(order.town_or_city, "Example town or city")
        self.assertEqual(order.street_address_1, "11 Example street")
        self.assertEqual(order.street_address_2, "apartment 11")
        self.assertEqual(order.county, "Example County")
        
    def test_order_model_as_string(self):
        current_date=timezone.now()
        order = Order(full_name="Katie Kelly", phone_number=22442244, country="Example Country", postcode="12ABC34", town_or_city="Example town or city", street_address_1="11 Example street", street_address_2="apartment 11", county="Example County", date=current_date)
        order.save()
        self.assertEqual(str(order.id)+"-"+str(order.date)+"-Katie Kelly", str(order))
        
    
  