from unittest import TestCase
from ObjectHandler import ObjectHandler

class TestObjectHandler(TestCase):
    def test_setupScreen(self):
        example = ObjectHandler()
        self.assertTrue(example.setupScreen())

    def test_run(self):
        example = ObjectHandler()
        self.assertTrue(example.run())
