# File: UI.py
# Author: BearsOnUnicyles
# Since: 4/16/18
# This module controls the user interface for the arena

from . import health_bar
from src import engine

class UI(engine.game_object.GameObject):

    bar1 = None
    bar2 = None

    def __init__(self, player1, player2):
        super(UI, self).__init__("UI", set_active=True)
        bar1 = health_bar.HealthBar(player1, player1=True)
        bar2 = health_bar.HealthBar(player2, player2=True)
        self.add_child(bar1)
        self.add_child(bar2)
        self.add_component(engine.transform.Transform())

    def update(self):
        super(UI, self).update()

