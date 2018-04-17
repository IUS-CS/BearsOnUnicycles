# File: collider.py
# Author: BearsOnUnicycles
# Since: 3/13/18
# This file defines the collider classes used in the engine


from . import component as ct
from . import transform


class Collider(ct.Component):

    lowerP = (0, 0)  # bottom left vertex of the collider
    upperP = (1, 1)  # top right vertex of the collider
    cfunc = None     # a collision function passed by the implementer
    colliding = False
    collisions = []
    transform = None
    _start_lowerP = (0, 0)
    _start_upperP = (0, 0)
    _w = 0
    _h = 0

    def __init__(self, lowerP, upperP, cfunc):
        super(Collider, self).__init__(set_active=True)
        self._start_lowerP = self.lowerP = lowerP
        self._start_upperP = self.upperP = upperP
        self._w = abs(self.lowerP[0] - self.upperP[0])
        self._h = abs(self.lowerP[1] - self.upperP[1])
        self.colliding = False
        self.collisions = []
        self.cfunc = cfunc

    def __str__(self):
        return super(Collider, self).__str__() + "Lower Point: " + str(self.lowerP) + \
            "Upper Point: " + str(self.upperP)

    def check_collision(self):
        """checks to see if colliding with an
        object, uses decorated function cfunc"""
        self.collisions = self.cfunc(self.game_object)
        self.colliding = not (len(self.collisions) == 0)

    def update(self):
        self.transform = self.game_object.get_component(transform.Transform)
        self.lowerP = (self.transform.x, self._h + self.transform.y)
        self.upperP = (self._w + self.transform.x, self.transform.y)
        scale = self.transform.scale
        self._w = self._w * scale
        self._h = self._h * scale
        self.check_collision()
