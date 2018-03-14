# File: game_object.py
# Author: BearsOnUnicycles
# Since: 3/10/18
# this is the template file for all game_objects in the system which are stored in scenes


import component as ct
import transform as tr


class GameObjectError(Exception):
    pass


NOT_COMPONENT = "The component attempted to add does not inherit from component.Component!"
COMPONENT_NOT_FOUND = "The component does not exist or was not added to the game object!"
CHILD_NOT_FOUND = "The child does not exist or was not added to this game object!"
TRANSFORM_NOT_FOUND = "This object does not have a transform and cannot update!"


class GameObject:

    name = ""               # the name of our object
    components = []         # a reference to every component the game object has
    children = []           # a reference to any children this game object has
    active = False          # is the game_object currently in play
    worldPos = (0, 0)       # the absolute x, y position of the object (see transform)

    def __init__(self, name, set_active=False):
        self.name = name
        if set_active:
            self.active = True

    def __str__(self):
        return self.name + "\nComponents: " + str([str(c) for c in self.components]) + \
            "\nActive: " + str(self.active) + "\nWorld Pos: " + str(self.worldPos)

    def set_active(self, active):
        self.active = active

    def get_child_by_name(self, name):
        '''Gets a game objects child by name'''
        for child in self.children:
            if child.name is name:
                return child
        raise GameObjectError(CHILD_NOT_FOUND)

    def get_children_with_component(self, cType):
        '''Get all children with a certain component'''
        temp = []
        for child in self.children:
            if child.has_component(cType):
                temp.append(child)
        return temp

    def add_component(self, component):
        '''adds a component to the game object'''
        if not isinstance(component, ct.Component):
            raise GameObjectError(NOT_COMPONENT)
        self.components.append(component)

    def has_component(self, cType):
        '''returns whether a game object has
        a certain component'''
        for c in self.components:
            if type(c) is cType:
                return True
        return False

    def get_component(self, cType):
        '''gets a component by type only, throws an exception
        if the type doesn't exist'''
        for c in self.components:
            if type(c) is cType:
                return c
        raise GameObjectError(COMPONENT_NOT_FOUND)

    def update(self):
        '''perform any logic on every child and component
        for one frame'''
        if self.active:
            try:
                # Sets the world position for this object
                self.worldPos = (self.get_component(tr.Transform).x, self.get_component(tr.Transform).y)
                for c in self.children:
                    c.update()
                    # Adjusts the world position of the children
                    c.worldPos = (c.worldPos[0] + self.worldPos[0], c.worldPos[1] + self.worldPos[1])
                for com in self.components:
                    com.update()
            except GameObjectError:
                raise GameObjectError(TRANSFORM_NOT_FOUND)



