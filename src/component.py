# File: component.py
# Author: BearsOnUnicycles
# Since: 3/10/18
# this is the template class for every component of a game_object


class Component:

    active = False          # is the component currently active

    def __init__(self, set_active=False):
        if set_active:
            self.active = True

    def set_active(self, active):
        self.active = active
