# File: main.py
# Authors: BearsOnUnicycles
# Since: 3/10/18
# This file calls all the main components of the game
import os
import pygame
import input_handler as ih

# =================================================================================
# Static Variables section
#
#
# =================================================================================

SIZE = (900, 500)
FPS = 15
INPUT = ih.Handler()
SCREEN = None


# =================================================================================
# Initialize pygame
#
# =================================================================================
pygame.init()
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
path = os.path.dirname(os.path.realpath(__file__))
SCREEN = pygame.display.set_mode(SIZE)


# =================================================================================
# Game Loop
#
# =================================================================================
quitting = False
while not quitting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitting = True
    pygame.time.Clock().tick(FPS)  # run at FPS frames per second
    INPUT.handle_input()  # the input handler is listening




