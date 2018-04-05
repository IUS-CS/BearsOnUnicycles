#Need to look into not having to use pygame to load this
import pygame
from old import constants as c

class LevelCreation():

    def setupBackground(self, filename): #Need to look up exceptions for image loading to return T or F
        image = pygame.image.load(c.PATH + '/resources/levels/' + filename).convert()
        image = pygame.transform.scale(image, c._SIZE_)
        return image