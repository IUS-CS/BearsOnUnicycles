# File: start_menu.py
# Authors: BearsOnUnicycles
# Since: 3/25/28
# This file creates the start menu scene, a simple title screen where the user must press a button to continue

from src import engine
from src import input_handler


class StartMenu(engine.scene.Scene):

    def __init__(self):
        super(StartMenu, self).__init__("Start Menu", "/src/resources/levels/StartMenu.png", set_active=True)
        g = engine.game_object.GameObject("prompt", set_active=True)
        g.add_component(engine.transform.Transform(x=200, y=100))
        g.add_component(engine.sprite.Sprite("/src/resources/misc/StartPrompt.png", (0, 0), (512, 256), 1))
        self.add_game_object(g)

    def update(self):
        super(StartMenu, self).update()
        if len(input_handler.Handler().get_active_keys()):
            print("continue")
            pass
