# File: splash.py
# Authors: BearsOnUnicycles
# Since: 3/25/18
# This file displays the splash screen and plays the splash sound


from src import engine
import pygame


class Splash(engine.scene.Scene):

    manager = None  # scene manager
    frame_timer = 0
    time_limit = 0
    sound = None

    def __init__(self, manager, timer):
        super(Splash, self).__init__("Splash", "/src/resources/menu/EditedUnicycle.jpg", set_active=True)
        self.frame_timer = 0
        self.time_limit = timer
        self.manager = manager
        self.sound = (pygame.mixer.Sound(manager.root_path + "/src/resources/menu/bearz.wav"))
        self.sound.play()
        self.sound.fadeout(4000)


    def update(self):
        self.frame_timer += 1
        if self.frame_timer == self.time_limit:
            self.manager.change_to_active("Start Menu")
