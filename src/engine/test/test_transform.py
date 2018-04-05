from .. import transform,  game_object

from unittest import TestCase


class TestTransform(TestCase):

    def test_add_to_obj(self):
        g = game_object.GameObject("Test")
        g.add_component(transform.Transform(x=1, y=2))
        assert g.has_component(transform.Transform)

    def test_x_and_y_vals(self):
        g = game_object.GameObject("Test")
        g.add_component(transform.Transform(x=2, y=4))
        assert g.get_component(transform.Transform).x == 2
        assert g.get_component(transform.Transform).y == 4

    def test_nested_transform(self):
        g = game_object.GameObject("Test", set_active=True)
        g.add_component(transform.Transform(x=1, y=5))
        g2 = game_object.GameObject("Test2", set_active=True)
        g2.add_component(transform.Transform(x=4, y=6))
        g.add_child(g2)
        g.update()
        assert g2.get_component(transform.Transform).world_x == 5
        assert g2.get_component(transform.Transform).world_y == 11


