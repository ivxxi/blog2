import unittest
from app.models import Comment, User,Blog
from app import db


class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username='Ivxxi', password='mypassword', email='ivxxi@gmail.com')
        self.post_Fly = Blog(title='blog title test', body='blog body test', id='1')
        self.new_comment = Comment(body='blog comment', author='user ivxxi')

    def tearDown(self):
        Comment.query.delete()
        Post.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_comment.body, 'blog comment')
        self.assertEquals(self.new_comment.author, 'user ivxxi')



