import os
import pygame
from old import constants as c
from old import Level

class ObjectHandler(object):

    def __init__(self):
        pygame.init()

        #Needs to be moved at some point. I think I'm scared to touch it until
        #our character works.
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

        level = Level.LevelCreation()
        self.setupScreen(level)
        self.run()

    def setupScreen(self, level):
        self.screen = pygame.display.set_mode(c._SIZE_)

        #this will be changed. probably need try catch for file being present
        self.background = level.setupBackground('mongoliaTent.bmp')
        return True

    def run(self):
        done = False
        self.left = 150

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True


            pygame.time.Clock().tick(c._CLOCK_SPEED_)
            self.screen.blit(self.background, (0, 0))
            pygame.display.update()
        return


