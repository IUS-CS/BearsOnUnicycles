# File: selection_box.py
# Author: BearsOnUnicycles
# Since: 4/17/18
# this file defines the character selection box logic


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
SIZE_X = 186
SIZE_Y = 186
SPRITES = [
    ("idle", (40, 40), 1, (SIZE_X, SIZE_Y), "/src/resources/misc/rect.png",
     (256, 256), 1),
]
SPRITES2 = [
    ("idle", (40, 40), 1, (SIZE_X, SIZE_Y), "/src/resources/misc/rect2.png",
     (256, 256), 1),
]

STATES = [  # (title, next, frames)
    ("idle", "idle", 1),

]


class SelectionBox(selection_controller.SelectionControlller):

    def __init__(self, pos, size, player2=False):
        super(SelectionBox, self).__init__("SelectionBox", pos, size)
        if not player2:
            self.load_animations(SPRITES)
        else:
            self.load_animations(SPRITES2)
        self.load_states(STATES)

    def update(self):
        super(SelectionBox, self).update()