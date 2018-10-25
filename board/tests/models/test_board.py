from django.test import TestCase
from django.db import models

from ..factories import BoardFactory


class BoardModelTest(TestCase):
    """
    This class defines the test suite for the board model.
    """

    board = None

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        BoardModelTest.board = BoardFactory.build()

    def test_name_field(self):
        field = BoardModelTest.board._meta.get_field("name")
        self.assertIsInstance(field, models.CharField)
        self.assertEqual(field.max_length, 30)
        self.assertTrue(field.unique)

    def test_description_field(self):
        field = BoardModelTest.board._meta.get_field("description")
        self.assertIsInstance(field, models.CharField)
        self.assertEqual(field.max_length, 100)

    def test_model_returns_readable_representation(self):
        """Test a readable string is returned for the model instance."""
        self.assertEqual(str(BoardModelTest.board), BoardModelTest.board.name)
