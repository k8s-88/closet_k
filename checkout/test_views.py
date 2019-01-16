from django.test import TestCase

# Create your tests here.
class TestCheckoutViews(TestCase):
    
    def test_get_checkout_page(self):
        page = self.client.get("/cart/checkout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout/checkout.html")