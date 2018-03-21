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

    def __init__(self, lowerP, upperP, cfunc):
        super(Collider, self).__init__(set_active=True)
        self.lowerP = lowerP
        self.upperP = upperP
        self.colliding = False
        self.collisions = []
        self.cfunc = cfunc

    def __str__(self):
        return super.__str__() + "Lower Point: " + str(self.lowerP) + \
            "Upper Point: " + str(self.upperP)

    def check_collision(self):
        '''checks to see if colliding with an
        object, decorated function'''
        self.collisions = self.cfunc(self.game_object)
        self.colliding = not (len(self.collisions) == 0)

    def update(self):
        scale = self.game_object.get_component(transform.Transform).scale
        self.upperP = (self.upperP[0] * scale, self.upperP[1] * scale)
        self.check_collision()
