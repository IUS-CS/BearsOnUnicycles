"""
Spritesheet Creation Library
Initial Commit: Jared Sanders

This class is designed to take a given spritesheet, cut the images,
and load each character in the row. Thought about pyganim, but this
is almost as easy as using that.

This file is very, very likely to change frequently
"""

import pygame

import constants

class Spritesheet(object):

  def __init__(self, file_name):
    """Need to look up try catch blocks to verify syntax"""

    self.sprite_sheet = pygame.image.load(file_name).convert()
 
  def get_image(self, x, y, width, height):

    image = pygame.Surface([width, height]).convert()

    image.blit(self.sprite_sheet, (0,0), (x,y,width,height))

    image.set_colorkey(c.BLACK)

    return image
 
