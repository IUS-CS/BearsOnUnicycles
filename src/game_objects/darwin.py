# File: darwin.py
# Author: BearsOnUnicycles
# Since: 4/18/18
# This module defines the character Darwin including his animations and logic

from . import character

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
SIZE_X = 360
SIZE_Y = 450
DARWIN_ANIMATIONS = [
    ("idle", (SIZE_X * 0, SIZE_Y * 0), 1, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/darwin/darwin basic1.png",
     (2880, 3150),    1),
    ("punch1", (SIZE_X * 4, SIZE_Y * 1), 4, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/darwin/darwin basic1.png",
     (2880, 3150), 1),
    ("punch2", (SIZE_X * 7, SIZE_Y * 1), 8, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/darwin/darwin basic1.png",
     (2880, 3150), 1),
    ("crouch", (SIZE_X * 1, SIZE_Y * 3), 1, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/darwin/darwin basic1.png",
    (2880, 3150), 1),
    ("crouch_punch1", (SIZE_X * 2, SIZE_Y * 3), 4, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/darwin/darwin basic1.png",
    (2880, 3150), 1),
    ("crouch_punch2", (SIZE_X * 6, SIZE_Y * 3), 8, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/darwin/darwin basic1.png",
    (2880, 3150), 1),
    ("jump", (SIZE_X * 6, SIZE_Y * 4), 1, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/darwin/darwin basic1.png",
    (2880, 3150), 1),
    ("air_idle", (SIZE_X * 3, SIZE_Y * 6), 1, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/darwin/darwin basic1.png",
    (2880, 3150), 1),
    ("air_punch1", (SIZE_X * 1, SIZE_Y * 5), 4, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/darwin/darwin basic1.png",
    (2880, 3150), 1),
    ("air_punch2", (SIZE_X * 3, SIZE_Y * 5), 8, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/darwin/darwin basic1.png",
    (2880, 3150), 1),
    ("walk", (SIZE_X * 0, SIZE_Y * 0), 6, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/darwin/darwin basic1.png",
    (2880, 3150), 1),
]


STATES = [  # (title, next, frames)
    ("idle", "idle", 1),
    ("punch1", "idle", 4),
    ("punch2", "idle", 8),
    ("crouch", "idle", 1),
    ("crouch_punch1", "crouch", 4),
    ("crouch_punch2", "crouch", 8),
    ("jump", "air_idle", 4),
    ("air_idle", "air_idle", 1),
    ("air_punch1", "air_idle", 4),
    ("air_punch2", "air_idle", 8),
    ("walk", "idle", 6),

]


class Darwin(character.Character):

    jump_counter = 1

    def __init__(self, pos, size, collision_manager):
        super(Darwin, self).__init__("Darwin", pos, size, collision_manager)
        self.load_animations(DARWIN_ANIMATIONS)
        self.load_states(STATES)

    def update(self):
        super(Darwin, self).update()

