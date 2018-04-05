from .. import component
from unittest import TestCase


class TestComponent(TestCase):
    def test_set_active_True(self):
        com = component.Component()
        com.set_active(True)
        assert com.active

    def test_set_active_False(self):
        com = component.Component()
        com.set_active(False)
        assert not com.active
