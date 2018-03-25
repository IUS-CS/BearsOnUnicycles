# File: animation_controller.py
# Authors: BearsOnUnicycles
# Since: 3/24/18
# This file renders the animations for a game object using pygame
import pygame
from . import sprite_renderer, animator


class LoadableAnimator(pygame.sprite.Group):

    title = ""
    sprites = []  # the sprites this animation contains
    anim = None   # the animator attached to the game object

    def __init__(self, path, anim, title):
        self.title = title
        self.sprites = []
        self.anim = anim
        for spr in anim:
            load = sprite_renderer.Loadable(path, spr)
            self.sprites.append(load)

    def update(self):
        for spr in self.sprites:
            spr.update()


class AnimationPlayer:

    game_objects = {}  # key = name, value = {title, LoadableAnimation object}
    sc = None

    def __init__(self, sc):
        self.sc = sc
        for g in sc.game_objects:
            for ga in g.children:
                self.load_anim(ga)
            self.load_anim(g)

    def load_anim(self, game_object):
        self.load_anim(game_object)
        anim = g.get_component(animator.Animator)
        self.game_objects[game_object.name] = {}
        for key, value in anim.animations:
            self.game_objects[game_object.name][key] = LoadableAnimator(value.path, value, key)





