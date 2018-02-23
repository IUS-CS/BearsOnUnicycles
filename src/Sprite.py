import os
import pygame


class Sprite(object):
    #Cuts each sprite at x, y. Going to try
    #making the list x, y, xwid, ywid, and changing
    #character rect below to the coords[2], coords[3]
    #to see if it fixes the clipping

    coords = {'idle': ( #corresponds to idle anim location
            (0, 15, 47, 84),
            (49, 15, 47, 84),
            (99, 15, 47, 84),
            (148, 15, 47, 84)
        ), 'walking': ( #corresponds to walking anim location
            (202, 15, 44, 84),
            (249, 15, 44, 84),
            (298, 15, 44, 84),
            (348, 15, 44, 84),
            (398, 15, 44, 84)
        ),'kick':( #corresponds to kick anim location
            (7, 252, 53, 97),
            (61, 252, 75, 91),
            (136, 252, 50, 88)
            )
    }

    def build_spriteset(self):
        path = os.path.dirname(os.path.realpath(__file__))
        spriteset = pygame.image.load(path + '/resources/misc/ryu.gif').convert()
        transparent_pixel = (0, 0)
        spriteset.set_colorkey(spriteset.get_at(transparent_pixel))
        sprites = dict()
        for name, coords in self.coords.items():
            sprites[name] = list()
            for coord in coords:
                rect = pygame.Rect(coord[0], coord[1], coord[2], coord[3])
                sprite = spriteset.subsurface(rect).convert()
                sprite = pygame.transform.scale(sprite, (256,256))
                sprites[name].append(sprite)

        return sprites
