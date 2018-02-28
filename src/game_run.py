import pygame
pygame.init()
pygame.display.set_mode()
from ObjectHandler import ObjectHandler
from SplashScreen import SplashScreen

Splash = SplashScreen().setupScreen()

if __name__ == '__main__':

    objectHandler = ObjectHandler()
    objectHandler.run()
    pygame.quit()
