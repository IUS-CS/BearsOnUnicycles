# File: sprite_renderer.py
# Authors: BearsOnUnicycles
# Since: 3/17/18
# This file renders sprites to the screen using pygame's rendering system


from . import scene, sprite, game_object, transform
import pygame
import os


class RendererError(Exception):
    pass


FILE_NOT_FOUND = "The specified file path does not exist!"


# see pygame.org/docs/ref/sprite.html
class Loadable(pygame.sprite.Sprite):

    location = (0, 0)
    spr = None
    image = None
    scale = (0, 0)
    flip = False
    priority = 0
    trans = None

    def __init__(self, path, spr, location):
        '''takes a file path, a sprite object,
        a sprite sheet where the object is located,
        and a location where the obj will be rendered

        loads the file where the sprite is located
        and pushes it to te render queue'''
        super(Loadable, self).__init__()
        self.spr = spr
        try:
            sheet = pygame.image.load_extended(path).convert()
            sheet.set_colorkey(sheet.get_at((0, 0)))   # sets the alpha mask to the color of the first pixel
        except pygame.error:
            print(path)
            raise RendererError(FILE_NOT_FOUND)  # my error message more helpful than theirs

        rect = pygame.Rect(spr.coords[0], spr.coords[1],  spr.size[0], spr.size[1])
        self.trans = spr.game_object.get_component(transform.Transform)
        scale_t = self.trans.scale
        self.scale = (scale_t * spr.size[0], scale_t * spr.size[1])
        self.image = sheet.subsurface(rect)
        self.image.set_colorkey(sheet.get_at((0, 0)))  # same as above
        self.location = location
        self.priority = spr.render_priority
        self.flip = False

    def update(self, *args):
        '''renders self each frame'''
        self.location = (self.trans.world_x, self.trans.world_y)
        self.flip = self.trans.flip


class SpriteRenderer:

    background = None  # path to background image
    sprites = []       # render queue, items with lower priority get drawn first
    root_path = ""     # path to root of game
    sc = None          # reference to active scene
    surface = None     # reference to active surface (see pygame.org/doc/ref/Surface.html)

    def __init__(self, sc, surface):
        self.sprites = []
        self.root_path = os.path.abspath("..")
        self.sc = sc
        self.surface = surface
        self.load_background()
        self.load_sprites()

    def load_sprites(self):
        '''loads the sprite images into
        the renderer's queue'''
        for g in self.sc.game_objects:
            self.load_sprites_rec(g)
        self.sprites.sort(key=lambda x: x.priority, reverse=True)
        # the above sorts the render queue on render priority descending
        #  note: the background is hard coded to render first

    def load_sprites_rec(self, g):
        '''helps load sprites by recurring through
        the children'''
        for gC in g.children:
            self.load_sprites_rec(gC)
        if g.has_component(sprite.Sprite) and g.active:
            spr = g.get_component(sprite.Sprite)
            path = self.root_path + spr.path
            load = Loadable(path, spr, (0, 0))
            self.sprites.append(load)  # fills the list with Loadable objects

    def load_background(self):
        '''loads the background image'''
        back = pygame.image.load_extended(self.root_path + self.sc.background)
        back = pygame.transform.scale(back, self.surface.get_size())
        self.background = back

    def update(self):
        '''updates the sprites on the
        screen'''
        self.surface.blit(self.background, (0, 0))
        for spr in self.sprites:
            spr.update()
            spr.image = pygame.transform.scale(spr.image, (spr.scale[0], spr.scale[1]))
            spr.image = pygame.transform.flip(spr.image, False, spr.flip)
            self.surface.blit(spr.image, spr.location)






