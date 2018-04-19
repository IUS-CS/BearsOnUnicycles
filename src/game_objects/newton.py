# File: newton.py
# Author: BearsOnUnicycles
# Since: 4/18/18
# This module defines the character newton including his animations and logic

from . import character
from src import engine

"""
format for animation loading is:
        (title,       # the title of the animation
        start,       # the starting (x, y) in pixels
        count,       # the number of frames
        size,        # the pixel size of each frame
        path,        # the path to the sprite sheet
        sheet_size,  # the dimensions of the sprite sheet
        priority)
"""
SIZE_X = 524
SIZE_Y = 546
NEWTON_ANIMATIONS = [
    ("idle", (SIZE_X * 0, SIZE_Y * 0), 12, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/newton/isaac newton basic1.png",
     (4192, 4368),    1),
    ("punch1", (SIZE_X * 4, SIZE_Y * 2), 4, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/newton/isaac newton basic1.png",
     (4192, 4368), 1),
    ("punch2", (SIZE_X * 0, SIZE_Y * 3), 8, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/newton/isaac newton basic1.png",
     (4192, 4368), 1),
    ("crouch", (SIZE_X * 1, SIZE_Y * 4), 1, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/newton/isaac newton basic1.png",
    (4192, 4368), 1),
    ("crouch_punch1", (SIZE_X * 1, SIZE_Y * 4), 4, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/newton/isaac newton basic1.png",
    (4192, 4368), 1),
    ("crouch_punch2", (SIZE_X * 5, SIZE_Y * 4), 8, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/newton/isaac newton basic1.png",
    (4192, 4368), 1),
    ("jump", (SIZE_X * 4, SIZE_Y * 5), 1, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/newton/isaac newton basic1.png",
    (4192, 4368), 1),
    ("air_idle", (SIZE_X * 5, SIZE_Y * 7), 1, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/newton/isaac newton basic1.png",
    (4192, 4368), 1),
    ("air_punch1", (SIZE_X * 0, SIZE_Y * 6), 4, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/newton/isaac newton basic1.png",
    (4192, 4368), 1),
    ("air_punch2", (SIZE_X * 4, SIZE_Y * 6), 8, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/newton/isaac newton basic1.png",
    (4192, 4368), 1),
    ("walk", (SIZE_X * 2, SIZE_Y * 0), 3, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/newton/isaac newton basic1.png",
    (4192, 4368), 1),
]


STATES = [  # (title, next, frames)
    ("idle", "idle", 12),
    ("punch1", "idle", 4),
    ("punch2", "idle", 8),
    ("crouch", "idle", 1),
    ("crouch_punch1", "crouch", 4),
    ("crouch_punch2", "crouch", 8),
    ("jump", "air_idle", 4),
    ("air_idle", "air_idle", 1),
    ("air_punch1", "air_idle", 4),
    ("air_punch2", "air_idle", 8),
    ("walk", "idle", 3),

]


class Newton(character.Character):

    jump_counter = 1

    def __init__(self, pos, size, collision_manager):
        super(Newton, self).__init__("Newton", pos, size, collision_manager)
        self.load_animations(NEWTON_ANIMATIONS)
        self.load_states(STATES)
        self.get_component(engine.collider.Collider).w += 75

    def set_bounded(self, screen):
        super(Newton, self).set_bounded(screen)
        self.y_bounds = (self.y_bounds[0], self.y_bounds[1] - 50)

    def update(self):
        super(Newton, self).update()

