# File: transform.py
# Authors: BearsOnUnicycles
# Since: 3/11/18
# this file inherits from component.Component and represents the x,y position of a game_object

from . import component as ct


class Transform(ct.Component):

    x = 0           # The x position of the object relative to its parent
    y = 0           # The y position of the object relative to its parent
    world_x = 0     # The world x position of this game object
    world_y = 0     # The world x position of this game object

    def __init__(self, x=0, y=0):
        super(Transform, self).__init__(set_active=True)
        self.x = x
        self.y = y

    def __str__(self):
        return super(Transform, self).__str__() + \
            "Pos(x,y) = (" + str(self.x) + "," + str(self.y) + ')'

    def update(self):
        '''udate the transform of this
        game object'''
        self.world_x = self.x + self.game_object.get_component(Transform).x
        self.world_y = self.y + self.game_object.get_component(Transform).y
