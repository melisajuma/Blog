import unittest
from app.models import Blog, Comment
from app import db
from datetime import datetime


class BlogTest(unittest.TestCase):
    def setUp(self):
        self.new_blog = Blog(id=40, title='New Blog', content='This is the content',
                             category='Travel', posted=datetime.now())

    def tearDown(self):
        db.session.delete(self.new_blog)
        db.session.commit()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blog))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'New Blog')
        self.assertEquals(self.new_blog.content, 'This is the content')
        self.assertEquals(self.new_blog.category, 'Travel')
        self.assertEquals(self.new_blog.posted, datetime.now())

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        blog = Blog.get_blog(40)
        self.assertTrue(blog is not None)


class CommentsTest(unittest.TestCase):
    def setUp(self):
        self.new_blog = Blog(id=40, title='New Blog', content='This is the content',
                             category='Travel', posted=datetime.now())
        self.new_comment = Comment(
            name='Test Comment', comment='This is my Test comment', blog=new_blog)

    def tearDown(self):
        db.session.delete(self.new_blog)
        db.session.commit()
        db.session.delete(self.new_comment)
        db.session.commit()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.name, 'Test Comment')
        self.assertEquals(self.new_comment.comment, 'This is my Test comment')
        self.assertEquals(self.new_comment.blog, new_blog)


class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password='passtest')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('passtest'))
