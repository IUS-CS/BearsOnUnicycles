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
        super(SelectionBox, self).update()