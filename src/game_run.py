from Level import Level #import Level class
import pygame

if __name__ == '__main__':
    level = Level() #creates instance of the game loop class
    level.run() # start the game loop
    pygame.quit() # called when player presses the X button