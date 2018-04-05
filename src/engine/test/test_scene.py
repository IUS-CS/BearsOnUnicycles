from engine import scene
from engine import game_object
from engine import component
from unittest import TestCase


class TestScene(TestCase):
    def test_set_active_True(self):
        s = scene.Scene("Test", "None")
        s.set_active(True)
        assert s.active

    def test_set_active_False(self):
        s = scene.Scene("Test", "None")
        s.set_active(False)
        assert not s.active

    def test_add_game_object(self):
        s = scene.Scene("Test", "None")
        g = game_object.GameObject("Test1")
        s.add_game_object(g)
        assert g in s.game_objects

    def test_remove_game_object_by_name(self):
        s = scene.Scene("Test", "None")
        g = game_object.GameObject("Test1")
        s.add_game_object(g)
        assert g in s.game_objects
        s.remove_game_object_by_name("Test1")
        assert g not in s.game_objects

    def test_get_object_by_name(self):
        s = scene.Scene("Test", "None")
        g = game_object.GameObject("Test1")
        s.add_game_object(g)
        assert g in s.game_objects
        assert s.get_object_by_name("Test1") is g

    def test_get_objects_of_type(self):
        s = scene.Scene("Test", "None")
        g = game_object.GameObject("Test1")
        g.add_component(component.Component())
        s.add_game_object(g)
        l = s.get_objects_of_type(game_object.GameObject)
        assert g in l
