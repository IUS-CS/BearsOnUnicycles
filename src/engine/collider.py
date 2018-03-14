# File: collider.py
# Author: BearsOnUnicycles
# Since: 3/13/18
# This file defines the collider classes used in the engine


from . import component as ct


class Collider(ct.Component):

    lowerP = (0, 0)  # bottom left vertex of the collider
    upperP = (1, 1)  # top right vertex of the collider

    def __init__(self, lowerP, upperP):
        super(Collider, self).__init__(set_active=True)
        self.lowerP = lowerP
        self.upperP = upperP

    def __str__(self):
        return super.__str__() + "Lower Point: " + str(self.lowerP) + \
            "Upper Point: " + str(self.upperP)

    def check_collision(self):
        '''checks to see if colliding with an
        object'''
        pass

