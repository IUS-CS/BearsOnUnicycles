# File: arena.py
# Authors: BearsOnUnicycles
# Since: 4/7/18
# This module is the main fighting arena for character objects -- Most of the game will be spent in this scene...
#       so don't f*** it up :)


from src import engine
import pygame


class Arena(engine.scene.Scene):

    player1 = None          # from game_objects.character.Character
    player2 = None
    UI = None               # from game_objects.UI.UI

    manager = None

    def __init__(self, manager, background, player1, player2, UI):
        super(Arena, self).__init__("arena", background, set_active=True)
        self.manager = manager
        self.player1 = player1
        self.player2 = player2
        if player1 is not None:
            self.add_game_object(player1)
        if player2 is not None:
            self.add_game_object(player2)
        self.UI = UI
        if UI is not None:
            self.add_game_object(UI)

    def update(self):
        super(Arena, self).update()


