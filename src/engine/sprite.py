# File: sprite.py
# Author: BearsOnUnicycles
# Since: 3/17/18
# This file is the basic wrapper for a sprite in the system.

from . import component as ct


class Sprite(ct.Component):

    path = ""           # the path to the sprite sheet
    coords = (0, 0)     # the pixel coords of the sprite
    size = (128, 128)   # the pixel size of the sprite
    render_priority = 0

    def __init__(self, path, coords, size, rp):
        super(Sprite, self).__init__(set_active=True)
        self.path = path
        self.coords = coords
        self.size = size
        self.render_priority = rp

    def __str__(self):
        return "Sprite located at " + str(self.coords) + \
            " on sheet " + self.path + " with size " + str(self.size)

    def replace(self, spr):
        self.path = spr.path
        self.coords = spr.coords
        self.size = spr.size
        self.render_priority = spr.render_priority

