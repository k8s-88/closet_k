from django.shortcuts import get_object_or_404
from django.test import TestCase
from .models import Post, Comment
from django.utils import timezone
from django.contrib.auth.models import User
# Create your tests here.
class TestBlogViews(TestCase):
    

        
    def test_all_blog_posts_returns_301_status_code(self):
        page = self.client.get("/blog/posts")
        self.assertEqual(page.status_code, 200)
        
        
        
    def test_get_single_blog_post_page(self):
        p_date = timezone.now()
        post = Post(title="Example Blog", content="Example Blog Content", published_date=p_date)
        post.save()
        page = self.client.get("/posts/{0}/".format(post.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blog/read_post.html")

        
        
  