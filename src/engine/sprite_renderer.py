# File: sprite_renderer.py
# Authors: BearsOnUnicycles
# Since: 3/17/18
# This file renders sprites to the screen using pygame's rendering system


from . import sprite, transform
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
    size = (0, 0)
    max_size = (0, 0)
    diff = (0, 0)

    def __init__(self, path, spr, location):
        """takes a file path, a sprite object,
        a sprite sheet where the object is located,
        and a location where the obj will be rendered

        loads the file where the sprite is located
        and pushes it to te render queue"""
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
        self.flip = spr.flip
        self.max_size = self.size = self.spr.size
        self.diff = (0, 0)


    def update(self):
        """renders self each frame"""
        self.location = (self.trans.world_x, self.trans.world_y)
        self.size = self.spr.size
        self.diff = (self.max_size[0] - self.size[0], self.max_size[1] - self.size[1])


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
        """loads the sprite images into
        the renderer"s queue"""
        for g in self.sc.game_objects:
            self.load_sprites_rec(g)
        self.sprites.sort(key=lambda x: x.priority, reverse=True)
        # the above sorts the render queue on render priority descending
        #  note: the background is hard coded to render first

    def load_sprites_rec(self, g):
        """helps load sprites by recurring through
        the children"""
        for gC in g.children:
            self.load_sprites_rec(gC)
        if g.has_component(sprite.Sprite) and g.active:
            spr = g.get_component(sprite.Sprite)
            path = self.root_path + spr.path
            load = Loadable(path, spr, (0, 0))
            self.sprites.append(load)  # fills the list with Loadable objects

    def load_background(self):
        """loads the background image"""
        back = pygame.image.load_extended(self.root_path + self.sc.background)
        back = pygame.transform.scale(back, self.surface.get_size())
        self.background = back

    def draw_background(self):
        """renders the background"""
        self.surface.blit(self.background, (0, 0))

    def update(self):
        """updates the sprites on the
        screen"""
        for spr in self.sprites:
            spr.update()
            if spr.size[0] == 0 or spr.size[1] == 0:
                continue
            rend = pygame.transform.scale(spr.image, (spr.size[0], spr.size[1]))
            rend2 = pygame.transform.flip(rend, spr.flip, False)
            if spr.flip:
                self.surface.blit(rend2, (spr.location[0] + spr.diff[0], spr.location[1] + spr.diff[1]))
            else:
                self.surface.blit(rend2, spr.location)






