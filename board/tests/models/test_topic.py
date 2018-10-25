from django.test import TestCase
from django.db import models

from ..factories import TopicFactory


class TopicModelTest(TestCase):
    """
    This class defines the test suite for the topic model.
    """

    topic = None

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        TopicModelTest.topic = TopicFactory.build()

    def test_subject_field(self):
        field = TopicModelTest.topic._meta.get_field("subject")
        self.assertIsInstance(field, models.CharField)
        self.assertEqual(field.max_length, 255)

    def test_last_update_field(self):
        field = TopicModelTest.topic._meta.get_field("last_update")
        self.assertIsInstance(field, models.DateTimeField)
        self.assertTrue(field.auto_now_add)

    def test_board_field(self):
        field = TopicModelTest.topic._meta.get_field("board")
        self.assertIsInstance(field, models.ForeignKey)

    def test_starter_field(self):
        field = TopicModelTest.topic._meta.get_field("starter")
        self.assertIsInstance(field, models.ForeignKey)

    def test_model_returns_readable_representation(self):
        """Test a readable string is returned for the model instance."""
        self.assertEqual(
            str(TopicModelTest.topic), TopicModelTest.topic.subject)
