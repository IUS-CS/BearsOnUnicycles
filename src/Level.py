import os
import pygame
from Sprite import Sprite

from Animator import Animator

import itertools

class Level(object):

    # global window size
    SIZE = (900, 650)

    def __init__(self):
        pygame.init()
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

        self.setupScreen()
        path = os.path.dirname(os.path.realpath(__file__))
        self.setupBackground(path)
        self.setupStates()

    def setupScreen(self):
        self.screen = pygame.display.set_mode(self.SIZE)
        return True

    def setupBackground(self, path): #Need to look up exceptions for image loading to return T or F
        image = pygame.image.load(path + '/resources/levels/mongoliaTent.bmp').convert()
        self.background = pygame.transform.scale(image, self.SIZE)

    def setupStates(self):
        self.animator = Animator()

    def run(self):
        done = False
        #self.sprite = itertools.cycle(self.sprites['idle'])
        self.p1left = 150

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    return 0


            self.handleEvents()


            #FPS setting. 60 makesthe character look like the Energizer Bunny on coffee

            pygame.time.Clock().tick(15)
            self.screen.blit(self.background, (0, 0))

            #This stupid blit is broken and I don't know why.
            #self.p1left doesn't work for the destination tuple, and the animation won't play
            self.screen.blit(self.animator.idle().__next__(), (325, 325)) #just testing Idle animation currently
            pygame.display.update()
        return 1



    def handleEvents(self):
        pressed = pygame.key.get_pressed()

        self.p1left = self.animator.checkAnim('idle')

        if pressed[pygame.K_LEFT]:
            self.p1left = self.animator.checkAnim('left')
        elif pressed[pygame.K_RIGHT]:
            self.p1left = self.animator.checkAnim('right')
        elif pressed[pygame.K_r]:
            self.p1left = self.animator.checkAnim('kick')

        #As long as p1left isn't empty return true.
        #Going to check python docs on the syntax for this

