from unittest import TestCase
from old import ObjectHandler


class TestObjectHandler(TestCase):
    def test_setupScreen(self):
        example = ObjectHandler
        self.assertTrue(example.setupScreen())

    def test_run(self):
        example = ObjectHandler
        self.assertTrue(example.run())
