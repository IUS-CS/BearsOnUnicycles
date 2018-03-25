# File: animator.py
# Authors: BearsOnUnicycles
# Since: 3/17/18
# This file controls the animations for the game objects in the system and should only be used for objects that
#   employ dynamic animations. There must be a sprite object attached to the game object in order to animate it
#   Objects that are statically animated should only use the sprite component

from . import component as ct
from . import sprite, game_object
import pygame

class AnimatorError(Exception):
    pass


NO_SPRITE_COMPONENT = "This object does not have a sprite component attached!"
NO_IDLE_ANIMATION = "This animator has no idle animation!"


class Animation:

    title = ""
    start_coords = (0, 0)  # the starting position on the sprite sheet in pixels
    frame_count = 1        # the number of frames this animation contains
    cut_size = (128, 128)  # the width and height of the animation frames in pixels
    sprites = []
    path = ""

    def __init__(self, title, start, count, size):
        self.title = title
        self.start_coords = start
        self.frame_count = count
        self.cut_size = size
        self.sprites = []

    def load_sprites(self, path, sheet_size, priority):
        '''loads all the sprites for a given animation
        based on the path of the spite sheet and attributes
        of the animation'''
        self.path = path
        for i in range(self.frame_count):
            x_offset = i * self.cut_size[0]   # move i frames to the right
            x = (self.start_coords[0] + x_offset) % sheet_size[0]
            y_offset = ((self.start_coords[0] + x_offset) // sheet_size[0]) * self.cut_size[1]
            y = self.start_coords[1] + y_offset
            # the above moves y offset pixels down the sheet
            spr = sprite.Sprite(path, (x, y), self.cut_size, priority)
            self.sprites.append(spr)


class Animator(ct.Component):

    animations = {}  # key = title, value = Animation object
    priority = 0
    current = None
    current_frame = 0
    current_frame_count = 1

    def __init__(self):
        super(Animator, self).__init__(set_active=True)
        self.animations = {}
        self.sprite_target = None
        self.priority = 0
        self.current = None
        self.current_frame = 0
        self.current_frame_count = 1

    def add_animation(self, animation):
        '''adds a possible animation
        to the animator'''
        self.animations[animation.title] = animation

    def build_animation(self,
                        title,       # the title of the animation
                        start,       # the starting (x, y) in pixels
                        count,       # the number of frames
                        size,        # the pixel size of each frame
                        path,        # the path to the sprite sheet
                        sheet_size,  # the dimensions of the sprite sheet
                        priority):   # the render priority
        '''constructs a new animation by the given parameters and
        loads the animation with its sprites'''
        anim = Animation(title, start, count, size)
        anim.load_sprites(path, sheet_size, priority)
        self.add_animation(anim)

    def set_current(self, title):
        '''sets the current playing animation'''
        self.current = self.animations[title]
        self.current_frame = 0
        self.current_frame_count = self.current.frame_count

    def play(self, isPlaying):
        '''plays or pauses the current animation'''
        self.active = isPlaying

    def next_sprite(self):
        '''changes the sprite image attached to the
        game object to the next frame in the cycle'''
        self.current_frame = (self.current_frame + 1) % self.current_frame_count

    def update(self):
        if self.current is None:
            try:
                self.set_current("idle")
            except KeyError:
                raise AnimatorError(NO_IDLE_ANIMATION)
