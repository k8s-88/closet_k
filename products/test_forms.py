from django.test import TestCase
from .forms import SizeForm


    

class TestSizeForm(TestCase):

    def test_SizeForm_valid(self):
        form = SizeForm({'quantity' : 1, 'shoe_sizes': 3})
        self.assertTrue(form.is_valid())
