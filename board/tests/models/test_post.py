from django.test import TestCase
from django.db import models

from ..factories import PostFactory


class PostModelTest(TestCase):
    """
    This class defines the test suite for the post model.
    """

    post = None

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        PostModelTest.post = PostFactory.build()

    def test_name_field(self):
        field = PostModelTest.post._meta.get_field("message")
        self.assertIsInstance(field, models.TextField)
        self.assertEqual(field.max_length, 4000)

    def test_created_at_field(self):
        field = PostModelTest.post._meta.get_field("created_at")
        self.assertIsInstance(field, models.DateTimeField)
        self.assertTrue(field.auto_now_add)

    def test_updated_at_field(self):
        field = PostModelTest.post._meta.get_field("updated_at")
        self.assertIsInstance(field, models.DateTimeField)
        self.assertTrue(field.null)

    def test_topic_field(self):
        field = PostModelTest.post._meta.get_field("topic")
        self.assertIsInstance(field, models.ForeignKey)

    def test_created_by_field(self):
        field = PostModelTest.post._meta.get_field("created_by")
        self.assertIsInstance(field, models.ForeignKey)

    def test_updated_by_field(self):
        field = PostModelTest.post._meta.get_field("updated_by")
        self.assertIsInstance(field, models.ForeignKey)

    def test_model_returns_readable_representation(self):
        """Test a readable string is returned for the model instance."""
        self.assertEqual(str(PostModelTest.post), PostModelTest.post.message)
