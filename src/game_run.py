import pygame
pygame.init()  # turn all of pygame on.
pygame.display.set_mode()
from Level import Level
from SplashScreen import SplashScreen


if __name__ == '__main__':
    #Splash = SplashScreen().setupScreen()
    #pygame.time.wait(8000)
    level = Level()
    level.run()
    pygame.quit()
