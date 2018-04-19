# File: win_screen.py
# Author: BearsOnUnicycles
# Since: 4/17/18
# This module displays the screen after a player has won in Arena

from src import engine
from . import start_menu


class WinScreen(engine.scene.Scene):

    timer = 150  # frames
    timer_count = 0
    timer_bool = False
    manager = None

    def __init__(self, manager, timer=150):
        super(WinScreen, self).__init__("Win Screen", "src/resources/levels/win_screen.png", set_active=True)
        self.timer = timer
        self.timer_count = 0
        self.timer_bool = False
        self.manager = manager
        pass

    def update(self):
        super(WinScreen, self).update()
        self.timer_count += 1
        if self.timer_count >= self.timer:
            self.timer_bool = True
        if self.timer_bool:
            self.manager.change_to_active("Start Menu")
