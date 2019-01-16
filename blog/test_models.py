from django.test import TestCase
from .models import Post, Comment
from django.utils import timezone
from django.contrib.auth.models import User
# Create your tests here.

class Test_Post_Model(TestCase):
    
    def test_PostModel(self):
        c_date = timezone.now()
        p_date = timezone.now()
        post=Post(title="Example Blog", content="Example Blog Content", published_date=p_date)
        post.save()
        self.assertEqual(post.title, "Example Blog")
        self.assertEqual(post.content, "Example Blog Content")
        self.assertEqual(post.published_date, p_date)

        
    def test_Comment_Model(self):
        p_date = timezone.now()
        post=Post(title="Example Article", content="Example Content", published_date=p_date)
        post.save()
        comment=Comment(content="Example Comment", post = post)
        comment.save()
        self.assertEqual(comment.content, "Example Comment")
 
