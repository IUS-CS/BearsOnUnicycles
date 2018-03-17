# File: game_object.py
# Author: BearsOnUnicycles
# Since: 3/10/18
# this is the template file for all game_objects in the system which are stored in scenes


from . import component as ct


class GameObjectError(BaseException):
    pass


NOT_COMPONENT = "The component attempted to add does not inherit from component.Component!"
COMPONENT_NOT_FOUND = "The component does not exist or was not added to the game object!"
CHILD_NOT_FOUND = "The child does not exist or was not added to this game object!"
TRANSFORM_NOT_FOUND = "This object does not have a transform and cannot update!"
PARENT_NOT_GAME_OBJ = "The parent attempted to add is not a Game Object!"
CHILD_NOT_GAME_OBJ = "The child attempted to add is not a Game Object!"

class GameObject:

    name = ""               # the name of our object
    components = []         # a reference to every component the game object has
    children = []           # a reference to any children this game object has
    parent = None           # the parent of this game object
    scene = None            # the scene this game object is in
    active = False          # is the game_object currently in play

    def __init__(self, name, set_active=False, parent=None):
        self.name = name
        self.children = []
        self.components = []
        if set_active:
            self.active = True
        if not isinstance(parent, GameObject) and parent is not None:
            raise GameObjectError(PARENT_NOT_GAME_OBJ)
        if parent is not None:
            self.parent = parent

    def __str__(self):
        return self.name + "\nComponents: " + str([str(c) for c in self.components]) + \
            "\nActive: " + str(self.active)

    def set_active(self, active):
        self.active = active

    def set_parent(self, parent):
        '''sets the parent of this game
        object'''
        if not isinstance(parent, GameObject):
            raise GameObjectError(PARENT_NOT_GAME_OBJ)
        self.parent = parent

    def add_child(self, child):
        '''adds a child to this
        game object'''
        if not isinstance(child, GameObject):
            raise GameObjectError(CHILD_NOT_GAME_OBJ)
        child.set_parent(self)
        self.children.append(child)

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
        component.game_object = self
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
            for c in self.children:
                c.update()
            for com in self.components:
                com.update()



