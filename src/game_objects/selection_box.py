# File: selection_box.py
# Author: BearsOnUnicycles
# Since: 4/15/18
# this file defines the character Albert Einstein's animations, logic


from . import selection_controller

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
SIZE_X = 118
SIZE_Y = 118
SPRITES = [
    ("idle", (40, 40), 1, (SIZE_X, SIZE_Y), "/src/resources/misc/rect.png",
     (198, 198), 1)
]


STATES = [  # (title, next, frames)
    ("idle", "idle", 1)
]


class SelectionBox(selection_controller.SelectionControlller):

    jump_counter = 1

    def __init__(self, pos, size, collision_manager):
        super(SelectionBox, self).__init__("SelectionBox", pos, size, collision_manager)
        self.load_animations(SPRITES)
        self.load_states(STATES)

    def update(self):
        super(SelectionBox, self).update()