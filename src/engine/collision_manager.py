# File: collision_manager.py
# Authors: BearsOnUnicycles
# Since: 3/17/18
# This file runs the logic of collisions with collider objects through the pygame engine and updates during the
#   physics cycle
#   ***this module cannot be tested using pytest and should not be F"ed with lightly***

import pygame
from . import collider


class CollisionManager:

    rects = {}              # every collider in the scene
    backw_rects = {}        # this is a key value swap of rects
    sc = None               # the scene where these rects live

    def __init__(self, sc):
        self.sc = sc
        for g in sc.game_objects:
            self.load_game_object(g)

    def load_game_object(self, g):
        """adds a game object"s collider
        to the collision manager"""
        for gC in g.children:
            self.load_game_object(gC)
        if g.has_component(collider.Collider):
            c = g.get_component(collider.Collider)
            left = c.lowerP[0]
            top = c.upperP[1]
            width = abs(c.upperP[0] - c.lowerP[0])
            height = abs(c.upperP[1] - c.lowerP[1])
            r = pygame.Rect(left, top, width, height)
            self.rects[(r.x, r.y, r.w, r.h)] = g.name
            self.backw_rects[g.name] = r

    def check_collisions(self, g):
        """checks if a game object is colliding
        with another game object and returns the
        result of those collisions"""
        self.rects = {}
        for gc in self.sc.game_objects:
            self.load_game_object(gc)
        if g.name in self.backw_rects.keys():
            r = self.backw_rects[g.name]
            return r.collidedictall(self.rects)
        return []

    def update(self):
        pass



