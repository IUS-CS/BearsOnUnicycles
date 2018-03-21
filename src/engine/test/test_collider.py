from .. import game_object, collider, transform
from unittest import TestCase


def mock_check_collisions(mock):
    return []

def mock_check_collisions_V2(mock):
    return [((1, 2, 3, 4), "Name")]  # Generally what a collision looks like


class TestCollider(TestCase):
    def test_check_collision_False(self):
        g = game_object.GameObject("Test")
        g.add_component(collider.Collider((4, 4), (5, 5), mock_check_collisions))
        g.get_component(collider.Collider).check_collision()
        assert not g.get_component(collider.Collider).colliding

    def test_check_collision_True(self):
        g = game_object.GameObject("Test")
        g.add_component(collider.Collider((4, 4), (5, 5), mock_check_collisions_V2))
        g.get_component(collider.Collider).check_collision()
        assert g.get_component(collider.Collider).colliding

    def test_check_scaling(self):
        g = game_object.GameObject("Test", set_active=True)
        g.add_component(transform.Transform(x=4, y=4, scale=2))
        g.add_component(collider.Collider((4, 4), (5, 5), mock_check_collisions_V2))
        g.update()
        assert g.get_component(collider.Collider).upperP == (10, 10)
        assert g.get_component(collider.Collider).lowerP == (4, 4)
