# File: nametag.py
# Author: BearsOnUnicycles
# Since: 4/17/18
# This module displays a nametag in the arena scene

from src import engine


SPRITE_MAP = {"Curie": "/src/resources/misc/curie_nametag.png",
              "Einstein": "/src/resources/misc/einstein_nametag.png",
              "Darwin": "/src/resources/misc/darwin_nametag.png",
              "Hawking": "/src/resources/misc/hawking_nametag.png",
              "Newton": "/src/resources/misc/newton_nametag.png",
              "Pythagoras": "/src/resources/misc/pythag_nametag.png",
              "Tesla": "/src/resources/misc/tesla_nametag.png",
              }


class Nametag(engine.game_object.GameObject):

    def __init__(self, player, key):
        super(Nametag, self).__init__("{} nametag".format(player.name), set_active=True)
        self.add_component(engine.sprite.Sprite(SPRITE_MAP[key], (0, 0), (300, 50), 0))

    def update(self):
        super(Nametag, self).update()