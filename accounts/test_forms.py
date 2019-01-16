from django.test import TestCase
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User

# Create your tests here.
class TestAccountsForms(TestCase):
    
    def test_signup_form(self):
        form=SignUpForm({
            'username': 'admin',
            'email': 'admin@example.com',
            'password1': 'pa55word1',
            'password2': 'pa55word1'
        })
        self.assertTrue(form.is_valid())
        
        
        
    def profile_form(self):
        form=ProfileForm({
            'username': 'admin',
            'password': 'pa55word'
        })
        self.assertTrue(form.is_valid())    
        
    def test_signup_email_required(self):
        form = SignUpForm({'email':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])
        

        
    def test_sign_up_passwords_must_match(self):
        form = SignUpForm({
            'username': 'admin',
            'email': 'admin@example.com',
            'password1': 'pa55word1',
            'password2': 'pa55word2'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ["The two password fields didn't match."])

        

        
        
        
        
        
        