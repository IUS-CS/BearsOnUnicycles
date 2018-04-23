# File: tesla.py
# Author: BearsOnUnicycles
# Since: 4/15/18
# this file defines the character Albert tesla's animations, logic


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
SIZE_X = 378
SIZE_Y = 507
TESLA_ANIMATIONS = [
    ("idle", (SIZE_X * 0, SIZE_Y * 0), 24, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/tesla/tesla basic1.png",
     (3780, 4056), 1),
    ("punch1", (SIZE_X * 0, SIZE_Y * 3), 4, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/tesla/tesla basic1.png",
     (3780, 4056), 1),
    ("punch2", (SIZE_X * 4, SIZE_Y * 3), 8, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/tesla/tesla basic1.png",
     (3780, 4056), 1),
    ("crouch", (SIZE_X * 4, SIZE_Y * 4), 1, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/tesla/tesla basic1.png",
     (3780, 4056), 1),
    ("crouch_punch1", (SIZE_X * 5, SIZE_Y * 4), 4, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/tesla/tesla basic1.png",
     (3780, 4056), 1),
    ("crouch_punch2", (SIZE_X * 9, SIZE_Y * 4), 8, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/tesla/tesla basic1.png",
     (3780, 4056), 1),
    ("jump", (SIZE_X * 8, SIZE_Y * 5), 1, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/tesla/tesla basic1.png",
     (3780, 4056), 1),
    ("air_idle", (SIZE_X * 5, SIZE_Y * 7), 1, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/tesla/tesla basic1.png",
     (3780, 4056), 1),
    ("air_punch1", (SIZE_X * 1, SIZE_Y * 6), 4, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/tesla/tesla basic1.png",
     (3780, 4056), 1),
    ("air_punch2", (SIZE_X * 5, SIZE_Y * 6), 8, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/tesla/tesla basic1.png",
     (3780, 4056), 1),
    ("walk", (SIZE_X * 0, SIZE_Y * 0), 6, (SIZE_X, SIZE_Y), "/src/resources/spritesheets/tesla/tesla basic1.png",
     (3780, 4056), 1),
]


STATES = [  # (title, next, frames)
    ("idle", "idle", 24),
    ("punch1", "idle", 4),
    ("punch2", "idle", 8),
    ("crouch", "idle", 2),
    ("crouch_punch1", "crouch", 4),
    ("crouch_punch2", "crouch", 8),
    ("jump", "air_idle", 4),
    ("air_idle", "air_idle", 1),
    ("air_punch1", "air_idle", 4),
    ("air_punch2", "air_idle", 8),
    ("walk", "idle", 6),
]

class Tesla(character.Character):

    jump_counter = 1

    def __init__(self, pos, size, collision_manager):
        super(Tesla, self).__init__("Tesla", pos, size, collision_manager)
        self.load_animations(TESLA_ANIMATIONS)
        self.load_states(STATES)

    def update(self):
        super(Tesla, self).update()
