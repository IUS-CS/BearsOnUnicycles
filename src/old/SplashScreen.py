import pygame
import constants as c
import time



bear_roar = pygame.mixer.Sound('resources/menu/bearz.wav')
image = pygame.image.load('resources/menu/EditedUnicycle.jpg')


class SplashScreen(object):

    def __init__(self):
        pygame.init()
        self.setupScreen()

    def setupScreen(self):
        self.screen = pygame.display.set_mode(c._SIZE_)
        self.screen.blit(image, (0, 0))
        return True

    def run(self):
        start_time = pygame.time.get_ticks();
        self.setupScreen()
        pygame.display.update()

        return 1


        #bear_roar.play()




