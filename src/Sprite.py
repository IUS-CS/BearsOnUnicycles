import os
import pygame


class Sprite(object):
    #Cuts each sprite at x, y. Going to try
    #making the list x, y, xwid, ywid, and changing
    #character rect below to the coords[2], coords[3]
    #to see if it fixes the clipping

    coords = {'idle': ( #corresponds to idle anim location
            (0, 15),
            (49, 15),
            (99, 15),
            (148, 15)
        ), 'walking': ( #corresponds to walking anim location
            (202, 15),
            (249, 15),
            (298, 15),
            (348, 15),
            (398, 15)
        ),'kick':( #corresponds to kick anim location
            (7, 252),
            (61, 252),
            (136, 252)
        )
    }

    #Actually creates the character
    def build_spriteset(self):

        #Same as before. Sets path to current working directory
        path = os.path.dirname(os.path.realpath(__file__))

        #Sets spriteset to our spritesheet of choice and converts to proper format for pygame
        spriteset = pygame.image.load(path + '/resources/misc/ryu.gif').convert()

        #Not positive, pygame documentation wasn't clear, but tutorials all used it.
        #Believe it sets the transparency to the pixel at 0,0. Going to read more.
        transparent_pixel = (0, 0)

        #Believe this is what sets the background to transparent.
        spriteset.set_colorkey(
            spriteset.get_at(transparent_pixel)
        )

        #Initializes sprites as an empty dictionary.
        sprites = dict()

        #For each name in our coords dictionary
        for name, coords in self.coords.items():

            #Create a list for each name
            sprites[name] = list()

            #Iterate through each item in coords
            for coord in coords:

                #Set our rectangle to xloc, yloc, and arbitrary sizes.
                rect = pygame.Rect(coord[0], coord[1], 50, 90)

                #Makes the subsurface the rectangle
                sprite = spriteset.subsurface(rect).convert()

                #Scales our character to 256x256
                sprite = pygame.transform.scale(sprite, (256,256))

                #Append our sprite to the appropriate list
                sprites[name].append(sprite)
                
        #return the dictionray of lists so we can iterate through them
        return sprites
