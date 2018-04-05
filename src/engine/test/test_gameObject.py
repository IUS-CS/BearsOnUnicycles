from engine import game_object
from engine import component
from unittest import TestCase


class TestGameObject(TestCase):
    def test_set_active_True(self):
        g = game_object.GameObject("Test")
        g.set_active(True)
        assert g.active

    def test_set_active_False(self):
        g = game_object.GameObject("Test")
        g.set_active(False)
        assert not g.active

    def test_set_parent(self):
        g = game_object.GameObject("Test1")
        g2 = game_object.GameObject("Test2")
        g2.set_parent(g)
        assert g2.parent is g

    def test_set_parent_to_None(self):
        g = game_object.GameObject("Test1")
        g2 = game_object.GameObject("Test2")
        g2.set_parent(g)
        assert g2.parent is g
        try:
            g2.set_parent(None)
        except game_object.GameObjectError:
            assert True

    def test_add_child(self):
        g = game_object.GameObject("Test1")
        g2 = game_object.GameObject("Test2")
        g.add_child(g2)
        assert g2.parent is g

    def test_remove_child(self):
        g = game_object.GameObject("Test1")
        g2 = game_object.GameObject("Test2")
        g.add_child(g2)
        g.remove_child(g2)
        try:
            g.remove_child(g2)
            assert False
        except game_object.GameObjectError:
            assert True

    def test_get_child_by_name(self):
        g = game_object.GameObject("Test1")
        g2 = game_object.GameObject("Test2")
        g.add_child(g2)
        assert g2.parent is g
        assert g.get_child_by_name("Test2") is g2

    def test_get_children_with_component(self):
        g = game_object.GameObject("Test1")
        g2 = game_object.GameObject("Test2")
        g.add_child(g2)
        g2.add_component(component.Component())
        assert g2.parent is g
        try:
            l = g.get_children_with_component(component.Component)
        except game_object.GameObjectError:
            assert False
        assert l[0] is g2

    def test_add_component(self):
        g = game_object.GameObject("Test")
        g.add_component(component.Component())
        try:
            g.get_component(component.Component)
        except game_object.GameObjectError:
            assert False

    def test_has_component(self):
        g = game_object.GameObject("Test")
        g.add_component(component.Component())
        assert g.has_component(component.Component)

    def test_get_component(self):
        g = game_object.GameObject("Test")
        c = component.Component()
        g.add_component(c)
        assert g.get_component(component.Component) is c
