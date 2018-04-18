<<<<<<< HEAD
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
=======
# File: health_bar.py
# Author: BearsOnUnicycles
# Since: 4/16/18
# This module defines the logic for the health bar for each character

from src import engine
from . import character, nametag


PATH = "/src/resources/misc/rect.png"
P1_COORDS = (25, 25)
P2_COORDS = (635, 25)
SIZE = (118, 118)
BAR_SIZE = (310, 35)


class SelectionBox(engine.game_object.GameObject):

    width = character.MAX_HEALTH
    sprite = None
    character = None
    nametag = None

    def __init__(self, name, player1=False, player2=False):
        super(SelectionBox, self).__init__(name, set_active=True)
        self.character = character

        if player1:
            self.sprite = engine.sprite.Sprite(PATH, (40, 40), SIZE, 1)
            self.add_component(engine.transform.Transform(x=P1_COORDS[0], y=P1_COORDS[1]))
            self.add_component(self.sprite)
        if player2:
            self.sprite = engine.sprite.Sprite(PATH, (0, 0), SIZE, 1)
            self.add_component(engine.transform.Transform(x=P2_COORDS[0], y=P2_COORDS[1]))
            self.add_component(self.sprite)

    def update(self):
>>>>>>> b00aa72386da9f184f0442552fdde8bb9c5f0c99
        super(SelectionBox, self).update()