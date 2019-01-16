from django.test import TestCase
from .models import Product


class TestViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/home.html")
        
    def test_get_contact_page(self):
        page = self.client.get("/contact/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/contact.html")
        
        
    # def test_get_category_page(self):
        
    #     category = Category(name="Men", parent="Boots Men")
    #     category.save()
        
    #     page = self.client.get("/category/{0}".format(id))
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "products/view_category.html", {"category": category})    
        
    # def test_get_product_detail_page(self):

    #     product = Product(name="Heels",brand = "Nike", sku = "TBC", description = "TBC", price=50, stock = "1")
    #     product.save()

    #     page = self.client.get("/products/{0}".format(id))
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "products/product_detail.html", {"product": product})


 