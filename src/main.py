# File: main.py
# Authors: BearsOnUnicycles
# Since: 3/10/18
# This file calls all the main components of the game
import os
import pygame
from src import input_handler as ih
from src import engine

# =================================================================================
# Static Variables section
#
#
# =================================================================================

SIZE = (900, 500)
FPS = 15
INPUT = ih.Handler()
SCREEN = None
RENDER = None


# =================================================================================
# Initialize pygame
#
# =================================================================================
pygame.init()
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
path = os.path.dirname(os.path.realpath(__file__))
SCREEN = pygame.display.set_mode(SIZE)


# =================================================================================
# Start up game
#   This is where you would load level modules
# =================================================================================



# =================================================================================
# Game Loop
#
# =================================================================================
quitting = False
while not quitting:
    for event in pygame.event.get():  # Boiler plate pygame loop
        if event.type == pygame.QUIT:
            quitting = True
    pygame.time.Clock().tick(FPS)  # run at FPS frames per second
    pygame.display.update()  # tell the screen to repaint
    INPUT.handle_input()  # the input handler is listening
    # RENDER.update()       # the renderer is active



