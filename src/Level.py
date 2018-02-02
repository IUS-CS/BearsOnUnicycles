import os
import pygame
from Sprite import Sprite #import Sprite class
import itertools

class Level(object):

    # global window size
    SIZE = (900, 650)

    #Initialize the game
    def __init__(self):
        # initializes pygame so we can use it.
        pygame.init()

        #Initialize game window
        self.screen = pygame.display.set_mode(self.SIZE)

        #Only allow quitting, and key presses. Not really mandatory, but prevent
        #erroneous clicks
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

        #Initalize path variable to current working directory on any operating system
        path = os.path.dirname(os.path.realpath(__file__))

        #Sets image to currentDir/resources/levels/imageName and converts to proper format
        #for pygame to display
        image = pygame.image.load(path + '/resources/levels/mongoliaTent.bmp').convert()

        #Actually sets image as the background
        self.background = pygame.transform.scale(image, self.SIZE)

        #Was originally going to be used to set boundary. Had problems, not important yet
        left = (self.background.get_width() - self.SIZE[0]) / 2

        #Basic states to manage walking or kicking in handle_events
        self.walking = False
        self.kick = False

        #calls build_spriteset from Sprite.py. See Sprites for more information
        self.sprites = Sprite().build_spriteset()

    #Actual game loop function
    def run(self):
        #We're not done yet, so it's false
        done = False

        #Default state is idle. Cycle through idle first. See Sprite.py
        self.sprite = itertools.cycle(self.sprites['idle'])

        #Set our characters X to 0. See the Blit further down
        self.p1left = 0

        #Actual game loop
        while not done:
            #While we haven't quit, don't quit
            for event in pygame.event.get():
                #Called when quit button pressed
                if event.type == pygame.QUIT:
                    done = True

            #Handles animations currently. Will probably change eventually
            self.handleEvents()

            #FPS setting. 60 makesthe character look like the Energizer Bunny on coffee
            pygame.time.Clock().tick(15)

            #Blit actually draws the background. (0,0) is the location it's drawn
            self.screen.blit(self.background, (0, 0))

            #Blit actually draws the character. selft.p1left is the X location, 325 is an arbitrary
            #location at the moment. Feel free to change
            self.screen.blit(self.sprite.__next__(), (self.p1left, 325))

            #Display doesn't show anything without this line.
            pygame.display.update()

    #Currently handles animations
    def handleEvents(self):
        #Default animation state.
        move = 'idle'

        #Get what key is pressed on the keyboard.
        pressed = pygame.key.get_pressed()

        #If left arrow pressed. Can be K_a for WASD movement on a QWERTY keyboard
        if pressed[pygame.K_LEFT]:

            #Movement state for actual animation down below.
            move = 'left'

            #Update position on screen.
            self.p1left -= 9

        #If right arrow pressed. Can be K_d for WASD movement on a QWERTY keyboard
        if pressed[pygame.K_RIGHT]:

            #Movement state for actual animation down below.
            move = 'right'

            #Update position on screen.
            self.p1left += 9

        #If space pressed. Had jump anim, both are different sizes and the rect is thrown off.
        #Going to look into variably changing the rect size based on the image.
        if pressed[pygame.K_SPACE]:

            #Attempt to stop animation after one loop. Epicly failed. Still working on it
            if not self.kick:

                #Same attempt, similar result.
                self.kick = True

                #itertools iterates through each item in the list corresponding to 'kick'
                self.sprite = itertools.cycle(self.sprites['kick'])

        #Basic check if move = left or right, then moves and plays walking animations.
        #Need to create flipped version of walk right for walk left, and implement
        #seperate animations for both.
        if move in ('left', 'right'):

            #Correctly stops after one loop
            if not self.walking:

                #We're now walking
                self.walking = True

                #itertools iterates through each item in the list corresponding to 'walking'
                self.sprite = itertools.cycle(self.sprites['walking'])

         #Else we didn't press a walk button, or kick, so idle.
        else:

            #If we were walking, we're not anymore, set to idle.
            if self.walking:

                #Set walking to false so we stop moving
                self.walking = False

                #itertools iterates through each item in the list corresponding to 'idle'
                self.sprite = itertools.cycle(self.sprites['idle'])

