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
    scale = 1       # The scale of this game object
    flip = False    # is this positively or negatively oriented along y-axis?
    _last_flip = False      # the flip the frame before
    vel_x = 0       # the rate of change of x
    vel_y = 0       # the rate of change of y

    def __init__(self, x=0, y=0, scale=1):
        super(Transform, self).__init__(set_active=True)
        self.world_x = self.x = x
        self.world_y = self.y = y
        self.scale = scale
        self.vel_x = 0
        self.vel_y = 0
        self.flip = False
        self._last_flip = False

    def __str__(self):
        return super(Transform, self).__str__() + \
            "Pos(x,y) = (" + str(self.x) + "," + str(self.y) + ')'

    def flip_me(self):
        """Callback to the animator to flip"""
        if self._last_flip != self.flip:
            return True
        else:
            return False

    def set_flip(self, b):
        """Sets the value of flip and changes
        the value of last flip"""
        print(self.flip, self._last_flip)
        self._last_flip = self.flip
        self.flip = b


    def update(self):
        '''udate the transform of this
        game object'''
        self.x += self.vel_x
        self.y += self.vel_y
        self.world_x = self.x
        self.world_y = self.y
        if self.game_object.parent is not None:
            temp = self.game_object.parent
            while temp is not None:
                self.world_x += temp.get_component(Transform).x
                self.world_y += temp.get_component(Transform).y
                temp = temp.parent



