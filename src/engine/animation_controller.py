# File: animation_controller.py
# Authors: BearsOnUnicycles
# Since: 3/24/18
# This file renders the animations for a game object using pygame
import pygame
import os
from . import sprite_renderer, animator, transform


class LoadableAnimator(pygame.sprite.Group):

    title = ""
    root_path = ""
    sprites = []    # the sprites this animation contains
    anim = None     # the animator attached to the game object
    active = False  # is this animation currently playing?
    current_frame = 0
    frame_count = 1
    priority = 0
    location = (0, 0)

    def __init__(self, path, anim, title):
        super(LoadableAnimator, self).__init__()
        self.root_path = os.path.abspath("..")
        self.title = title
        self.sprites = []
        self.anim = anim
        self.location = (0, 0)
        for spr in anim.sprites:
            load = sprite_renderer.Loadable(self.root_path + path, spr, self.location)
            load.add(self)
            self.sprites.append(load)
        self.priority = anim.priority
        self.frame_count = anim.frame_count

    def get_current(self):
        return self.sprites[self.current_frame]

    def update(self):
        self.current_frame = (self.current_frame + 1) % self.frame_count
        self.active = self.anim.active
        for spr in self.sprites:
            spr.update()


class AnimationPlayer:

    game_objects = {}  # key = name, value = {title, LoadableAnimator object}
    sc = None          # the scene this game object is attached to
    sprites = []       # the animators render queue
    surface = None

    def __init__(self, sc, surface):
        self.sc = sc
        self.surface = surface
        for g in sc.game_objects:
            self.load_anim(g)
            for ga in g.children:   # recursively load children
                self.load_anim(ga)

    def load_anim(self, game_object):
        if game_object.has_component(animator.Animator):
            anim = game_object.get_component(animator.Animator)
            self.game_objects[game_object.name] = {}
            for key in anim.animations:
                self.game_objects[game_object.name][key] = LoadableAnimator(anim.animations[key].path,
                                                                            anim.animations[key], key)
                # the integer value represents the current frame step the animation is on

    def update(self):
        self.sprites = []
        for name in self.game_objects:
            for key in self.game_objects[name]:
                if self.game_objects[name][key].active:
                    self.sprites.append((self.game_objects[name][key].get_current(),
                                         self.game_objects[name][key].priority, (name, key)))
                self.game_objects[name][key].update()
        self.sprites.sort(key=lambda x: x[1])  # sort along render priority
        for spr in self.sprites:
            rend = spr[0].image.copy()
            if self.game_objects[spr[2][0]][spr[2][1]].anim.game_object.get_component(transform.Transform).flip:
                rend = pygame.transform.flip(spr[0].image, True, False)
            self.surface.blit(rend, spr[0].location)
