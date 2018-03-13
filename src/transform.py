# File: transform.py
# Authors: BearsOnUnicycles
# Since: 3/11/18
# this file inherits from component.Component and represents the x,y position of a game_object

import component as ct


class Transform(ct.Component):

    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        super(Transform, self).__init__(set_active=True)
        self.x = x
        self.y = y

    def __str__(self):
        return super(Transform, self).__str__() + \
            "Pos(x,y) = (" + str(self.x) + "," + str(self.y) + ')'


