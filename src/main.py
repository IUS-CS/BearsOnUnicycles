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

s = engine.scene.Scene("Test", "\\src\\resources\\levels\mongoliaTent.bmp", set_active=True)

g = engine.game_object.GameObject("Name", set_active=True)
g.add_component(engine.transform.Transform(x=50, y=50, scale=1))
#g.add_component(engine.sprite.Sprite("\\src\\resources\\spritesheets\\curie\\marie curie basic1.png",
#                                     (0, 0), (360, 586), 1))
g.add_component(engine.animator.Animator())
g.get_component(engine.animator.Animator).build_animation("idle", (0, 0), 6, (360, 586),
                                                          "\\src\\resources\\spritesheets\\curie\\marie curie basic1.png",
                                                          (3960, 4104),
                                                         1)

s.add_game_object(g)
RENDER = engine.sprite_renderer.SpriteRenderer(s, SCREEN)
ANIM = engine.animation_controller.AnimationPlayer(s, SCREEN)
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
    RENDER.update()       # the renderer is active
    ANIM.update()         # the animator is updating
    s.update()

