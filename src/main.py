# File: main.py
# Authors: BearsOnUnicycles
# Since: 3/10/18
# This file calls all the main components of the game
import os
import pygame
from src import scenes, game_objects
from src import input_handler as ih
from src import scene_manager as sm
import threading

# =================================================================================
# Static Variables section
#
#
# =================================================================================
pygame.init()
SIZE = (960, 540)
FPS = 24
PATH = os.path.abspath("..")
INPUT = ih.Handler()

# =================================================================================
# Initialize pygame
#
# =================================================================================

pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
pygame.display.set_caption("SUMOH")
icon = pygame.image.load_extended(PATH + "/src/resources/misc/icon.png")
pygame.display.set_icon(icon)
SCREEN = pygame.display.set_mode(SIZE)
MANAGER = sm.SceneManager(SCREEN, PATH)
SOUND = pygame.mixer.init(channels=4)  # 1 for music, 2 for FX, 3 for menu, 4 for overflow

# =================================================================================
# Start up game
#   This is where you would load level modules
# =================================================================================

MANAGER.add_scene(scenes.splash.Splash(MANAGER, 5 * FPS))  # 5 seconds
MANAGER.add_scene(scenes.start_menu.StartMenu(MANAGER))

# =================================================================================
# Game Loop
#
# =================================================================================
quitting = False
frames = 0
while not quitting:
    for event in pygame.event.get():  # Boiler plate pygame loop
        if event.type == pygame.QUIT:
            quitting = True
    pygame.time.Clock().tick(FPS)  # run at FPS frames per second
    pygame.display.update()  # tell the screen to repaint
    INPUT.handle_input()  # the input handler is listening
    MANAGER.update_scene()
