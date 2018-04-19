# File: hawking.py
# Author: BearsOnUnicycles
# Since: 4/18/18
# This module defines the character Hawking including his animations and logic

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
HAWKING_ANIMATIONS = [
    ("idle", (SIZE_X * 0, SIZE_Y * 0), 9, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/hawking/hawking basic1.png",
     (3240, 3150),    1),
    ("punch1", (SIZE_X * 0, SIZE_Y * 1), 4, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/hawking/hawking basic1.png",
     (3240, 3150), 1),
    ("punch2", (SIZE_X * 4, SIZE_Y * 1), 8, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/hawking/hawking basic1.png",
     (3240, 3150), 1),
    ("crouch", (SIZE_X * 1, SIZE_Y * 2), 1, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/hawking/hawking basic1.png",
    (3240, 3150), 1),
    ("crouch_punch1", (SIZE_X * 2, SIZE_Y * 2), 4, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/hawking/hawking basic1.png",
    (3240, 3150), 1),
    ("crouch_punch2", (SIZE_X * 0, SIZE_Y * 3), 8, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/hawking/hawking basic1.png",
    (3240, 3150), 1),
    ("jump", (SIZE_X * 1, SIZE_Y * 6), 1, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/hawking/hawking basic1.png",
    (3240, 3150), 1),
    ("air_idle", (SIZE_X * 2, SIZE_Y * 6), 1, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/hawking/hawking basic1.png",
    (3240, 3150), 1),
    ("air_punch1", (SIZE_X * 5, SIZE_Y * 4), 4, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/hawking/hawking basic1.png",
    (3240, 3150), 1),
    ("air_punch2", (SIZE_X * 1, SIZE_Y * 5), 8, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/hawking/hawking basic1.png",
    (3240, 3150), 1),
    ("walk", (SIZE_X * 0, SIZE_Y * 0), 6, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/hawking/hawking basic1.png",
    (3240, 3150), 1),
]


STATES = [  # (title, next, frames)
    ("idle", "idle", 9),
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


class Hawking(character.Character):

    jump_counter = 1

    def __init__(self, pos, size, collision_manager):
        super(Hawking, self).__init__("Hawking", pos, size, collision_manager)
        self.load_animations(HAWKING_ANIMATIONS)
        self.load_states(STATES)

    def set_bounded(self, screen):
        super(Hawking, self).set_bounded(screen)
        self.y_bounds = (self.y_bounds[0], self.y_bounds[1] - 35)

    def update(self):
        super(Hawking, self).update()

