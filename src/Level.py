import os
import pygame
from Sprite import Sprite
import itertools

class Level(object):
    SIZE = (900, 650)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.SIZE)
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
        path = os.path.dirname(os.path.realpath(__file__))
        image = pygame.image.load(path + '/resources/levels/mongoliaTent.bmp').convert()
        self.background = pygame.transform.scale(image, self.SIZE)
        left = (self.background.get_width() - self.SIZE[0]) / 2
        self.walking = False
        self.kick = False
        self.sprites = Sprite().build_spriteset()

    def run(self):
        done = False
        self.sprite = itertools.cycle(self.sprites['idle'])
        self.p1left = 0
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            self.handleEvents()
            pygame.time.Clock().tick(15)
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.sprite.__next__(), (self.p1left, 325))
            pygame.display.update()

    def handleEvents(self):
        move = 'idle'
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            move = 'left'
            self.p1left -= 9
        if pressed[pygame.K_RIGHT]:
            move = 'right'
            self.p1left += 9
        if pressed[pygame.K_SPACE]:
            if not self.kick:
                self.sprite = itertools.cycle(self.sprites['kick'])

        if move in ('left', 'right'):
            if not self.walking:
                self.walking = True
                self.sprite = itertools.cycle(self.sprites['walking'])
        else:
            if self.walking:
                self.walking = False
                self.sprite = itertools.cycle(self.sprites['idle'])

