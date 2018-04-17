# File: health_bar.py
# Author: BearsOnUnicycles
# Since: 4/16/18
# This module defines the logic for the health bar for each character

from src import engine
from . import character


PATH = "/src/resources/misc/health_fill2.png"
P1_COORDS = (25, 25)
P2_COORDS = (550, 25)
SIZE = (300, 25)
BAR_SIZE = (310, 35)


class HealthBar(engine.game_object.GameObject):

    width = character.MAX_HEALTH
    sprite = None
    character = None
    border = None

    def __init__(self, character, player1=False, player2=False):
        super(HealthBar, self).__init__(character.name, set_active=True)
        self.character = character

        if player1:
            self.sprite = engine.sprite.Sprite(PATH, (0, 0), SIZE, 1)
            self.add_component(engine.transform.Transform(x=P1_COORDS[0], y=P1_COORDS[1]))
            self.add_component(self.sprite)
        if player2:
            self.sprite = engine.sprite.Sprite(PATH, (0, 0), SIZE, 1)
            self.sprite.set_flip(True)
            self.add_component(engine.transform.Transform(x=P2_COORDS[0], y=P2_COORDS[1]))
            self.add_component(self.sprite)

        self.border = engine.game_object.GameObject("Border", set_active=True)
        sprite = engine.sprite.Sprite("/src/resources/misc/health_frame2.png", (0, 0), BAR_SIZE, 2)
        self.border.add_component(sprite)
        self.border.add_component(engine.transform.Transform(x=-5, y=-5))
        self.add_child(self.border)

    def update(self):
        super(HealthBar, self).update()
        self.sprite.size = (int(SIZE[0] * (self.width / character.MAX_HEALTH)), SIZE[1])
        self.width = self.character.health
