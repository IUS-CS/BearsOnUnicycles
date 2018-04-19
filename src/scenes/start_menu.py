# File: start_menu.py
# Authors: BearsOnUnicycles
# Since: 3/25/28
# This file creates the start menu scene, a simple title screen where the user must press a button to continue

import pygame

from src import engine, input_handler, scenes
import pygame as pg


class StartMenu(engine.scene.Scene):

    manager = None      # the scene manager
    sound = None

    def __init__(self, manager):
        super(StartMenu, self).__init__("Start Menu", "/src/resources/menu/Title Screen.png", set_active=True)
        self.sound = (pg.mixer.Sound(manager.root_path + "/src/resources/menu/Juhani Junkala [Retro Game Music Pack] Level 1.wav"))
        self.sound.play(25)



        g = engine.game_object.GameObject("prompt", set_active=True)
        g.add_component(engine.transform.Transform(x=200, y=100))
        #g.add_component(engine.sprite.Sprite("/src/resources/levels/StartMenu.png", (0, 0), (960, 540), 1))
        self.add_game_object(g)
        self.manager = manager

        self.sound = pygame.mixer.Sound(self.manager.root_path +
                                        "/src/resources/menu/Juhani Junkala [Retro Game Music Pack] Title Screen.wav")
        if pygame.mixer.get_busy():
            pygame.mixer.stop()
        self.sound.play(loops=-1)

    def update(self):
        super(StartMenu, self).update()
        if len(input_handler.Handler().get_active_keys()) > 0:
            print("load next scene")
            self.manager.add_scene(scenes.character_select.CharacterSelect(self.manager,
                                                                           "/src/resources/menu/characterSelect.png",
                                                                           "box1", "box2"))
            self.manager.change_to_active("CharacterSelect")
<<<<<<< HEAD
=======

<<<<<<< HEAD
>>>>>>> 501c3b7... Add additional resource files
=======
>>>>>>> 501c3b7... Add additional resource files
