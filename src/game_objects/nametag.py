# File: nametag.py
# Author: BearsOnUnicycles
# Since: 4/17/18
# This module displays a nametag in the arena scene

import engine


SPRITE_MAP = {"Curie": "/src/resources/misc/curie_nametag.png",
              "Einstein": "/src/resources/misc/einstein_nametag.png",
              }


class Nametag(engine.game_object.GameObject):


    def __init__(self, player, key):
        super(Nametag, self).__init__("{} nametag".format(player.name), set_active=True)
        self.add_component(engine.sprite.Sprite(SPRITE_MAP[key], (0, 0), (300, 50), 0))

    def update(self):
        super(Nametag, self).update()