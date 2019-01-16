from django.test import TestCase
from .forms import MakePaymentForm, OrderForm

# Create your tests here.
class TestCheckoutForms(TestCase):
    
    def test_make_payment_form(self):
        form=MakePaymentForm({
            'credit_card_number': '1234123412341234',
            'cvv': '123',
            'expiry_month': 10,
            'expiry_year': 2023,
            'stripe_id': 'TBC'
        })
        self.assertTrue(form.is_valid())
        
    def OrderForm(self):
        form=OrderForm({
            'full_name': 'Katie Kelly',
            'phone_number': '22442244',
            'street_address1': '11 Example street',
            'street_address2': 'apartment 11',
            'town_or_city': 'Example town or city',
            'county': 'Example County',
            'country': 'Example Country',
            'postcode': '12ABC34'
        })
        self.assertTrue(form.is_valid())    