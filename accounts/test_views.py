from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserCreationForm

# Create your tests here.
class TestAccountsViews(TestCase):
    
    def test_user_can_signup(self):
        response = self.client.post("/accounts/signup/", {
            'username': 'test',
            'email': 'test@email.com',
            'password1': 'Testpassword',
            'password2': 'Testpassword'
        })
        self.assertRedirects(response, '/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    
    def test_get_signup_page(self):
        page = self.client.get("/accounts/signup/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/signup.html")
        
    def test_get_profile_page(self):
        test_user = User.objects.create_user(username="test", email="test@example.com", password="Testpassword")
        self.client.login(username='test', password='Testpassword')
        page = self.client.get("/accounts/profile")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
 

 