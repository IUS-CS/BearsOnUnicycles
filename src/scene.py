# File: scene.py
# Authors: BearsOnUnicycles
# Since: 3/10/18
# This is the template file for all loadable scenes in the game and stores all the game_objects it controls

import game_object as go


class SceneError(Exception):
    '''Exceptions that can be thrown from scene'''
    pass


NOT_GAME_OBJECT = "The attempted object to add is not a game object!"
OBJ_NOT_FOUND = "The game object does not exist or was not added to the scene!"


class Scene:

    title = ""              # the title of the scene
    game_objects = []       # a reference to each game object in the scene
    background = ""         # the path to the background image
    active = False          # is this scene currently loaded?

    def __init__(self, title, background, set_active=False):
        self.title = title
        self.background = background
        if set_active:
            self.active = True

    def __str__(self):
        return self.title + "\nGame Objects: " + str([str(g) for g in self.game_objects]) + \
            "Active: " + str(self.active)

    def set_active(self, active):
        self.active = active

    def add_game_object(self, game_object):
        '''Adds a game obejct to the scene'''
        if not isinstance(game_object, go.GameObject):
            raise SceneError(NOT_GAME_OBJECT)
        self.game_objects.append(game_object)

    def remove_game_object_by_name(self, name):
        '''Removes a game_object from the scene
        throws an error if not found'''
        for g in self.game_objects:
            if g.name == name:
                self.game_objects.remove(g)
        raise SceneError(OBJ_NOT_FOUND)

    def get_object_by_name(self, name):
        '''gets a game obejct by name in
        the scene and throws an error if
        not found'''
        for g in self.game_objects:
            if g.name == name:
                return g
        raise SceneError(OBJ_NOT_FOUND)

    def get_objects_of_type(self, oType):
        '''gets a list of game_objects a specified
        type'''
        temp = []
        for g in self.game_objects:
            if type(g) is oType:
                temp.append(g)
        return temp


