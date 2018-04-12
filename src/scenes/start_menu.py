# File: start_menu.py
# Authors: BearsOnUnicycles
# Since: 3/25/28
# This file creates the start menu scene, a simple title screen where the user must press a button to continue

from src import engine
from src import input_handler


class StartMenu(engine.scene.Scene):

    manager = None      # the scene manager

    def __init__(self, manager):
        super(StartMenu, self).__init__("Start Menu", "/src/resources/levels/StartMenu.png", set_active=True)
        g = engine.game_object.GameObject("prompt", set_active=True)
        g.add_component(engine.transform.Transform(x=200, y=100))
        g.add_component(engine.sprite.Sprite("/src/resources/misc/StartPrompt.png", (0, 0), (512, 256), 1))
        self.add_game_object(g)
        self.manager = manager

    def update(self):
        super(StartMenu, self).update()
        if len(input_handler.Handler().get_active_keys()) > 0:
            #self.manager.change_to_active("play menu")
            self.manager.change_to_active("arena")
