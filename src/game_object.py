# File: game_object.py
# Author: BearsOnUnicycles
# Since: 3/10/18
# this is the template file for all game_objects in the system which are stored in scenes


import component as ct
import transform

class GameObjectError(Exception):
    pass


NOT_COMPONENT = "The component attempted to add does not inherit from component.Component!"
COMPONENT_NOT_FOUND = "The component does not exist or was not added to the game object!"


class GameObject:

    name = ""               # the name of our object
    components = []         # a reference to every component the game_object has
    active = False          # is the game_object currently in play

    def __init__(self, name, set_active=False):
        self.name = name
        if set_active:
            self.active = True

    def __str__(self):
        return self.name + "\nComponents: " + str([str(c) for c in self.components]) + \
            "\nActive: " + str(self.active)

    def set_active(self, active):
        self.active = active

    def add_component(self, component):
        '''adds a component to the game object'''
        if not isinstance(component, ct.Component):
            raise GameObjectError(NOT_COMPONENT)
        self.components.append(component)

    def get_component(self, cType):
        '''gets a component by type only, throws an exception
        if the type doesn't exist'''
        for c in self.components:
            if type(c) is cType:
                return c
        raise GameObjectError(COMPONENT_NOT_FOUND)




