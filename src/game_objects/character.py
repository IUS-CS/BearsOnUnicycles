# File: character.py
# Authors: BearsOnUnicycles
# Since: 4/7/18
# This is the base class for all characters in the game and should be inherited from for each individual character


from src import engine


class State:

    title = ""
    next = None
    change = False
    frames = 0
    counter = 0

    def __init__(self, title, next, frames):
        self.title = title
        self.next = next
        self.frames = frames
        self.change = False
        self.counter = 0

    def set_next(self, next):
        self.next = next

    def update(self):
        if self.counter > self.frames:
            self.change = True
        self.counter += 1

class Character(engine.game_object.GameObject):

    transform = None
    animator = None
    collider = None
    x_bounds = ()
    y_bounds = ()

    states = {}
    current = None
    next = None

    ignore_input = False  # ignore input until the state changes

    fall_speed = 25  # pixels per frame

    def __init__(self, name, pos, size, collision_manager):
        super(Character, self).__init__(name, set_active=True)
        self.size = size
        self.transform = t = engine.transform.Transform(pos[0], pos[1])
        self.add_component(t)
        self.animator = a = engine.animator.Animator()
        self.add_component(a)
        self.collider = c = engine.collider.Collider((pos[0], pos[1] + size[1]), (pos[0] + size[0], pos[1]), cfunc=collision_manager)
        self.add_component(c)
        self.x_bounds = ()
        self.y_bounds = ()
        self.states = {}

    def load_animations(self, anim_list):
        """Loads all a characters animations
        based of the values in anim_list
        must include an animation called
        'idle'

        format for animation loading is:
        (title,       # the title of the animation
        start,       # the starting (x, y) in pixels
        count,       # the number of frames
        size,        # the pixel size of each frame
        path,        # the path to the sprite sheet
        sheet_size,  # the dimensions of the sprite sheet
        priority)"""
        for anim in anim_list:
            self.animator.build_animation(anim[0], anim[1], anim[2], anim[3], anim[4], anim[5], anim[6])

    def load_states(self, states):
        """Loads states into the charcaters
        state machine"""
        for state in states:
            self.states[state[0]] = State(state[0], state[1], state[2])
        self.change_state("idle")

    def change_state(self, state):
        """changes the current state to
        #state"""
        self.current = self.states[state]
        self.next = self.states[self.current.next]
        self.animator.set_current(state)

    def state_machine(self):
        """this is where the logic of the
        character happens, it is left blank
        intentionally here"""
        pass

    def set_bounded(self, screen):
        """Ensures character stays on screen"""
        self.x_bounds = (-screen[0] / 2 + self.size[0] / 4, screen[0] / 2 - self.size[0] / 4)
        self.y_bounds = (-screen[1] / 2 + self.size[1] / 3, screen[1] / 2 - self.size[1] / 3)

    def check_bounds(self):
        """adheres the object to its borders"""
        if self.transform.x < self.x_bounds[0]:
            self.transform.x = self.x_bounds[0]
        if self.transform.x > self.x_bounds[1]:
            self.transform.x = self.x_bounds[1]
        if self.transform.y < self.y_bounds[0]:
            self.transform.y = self.y_bounds[0]
        if self.transform.y > self.y_bounds[1]:
            self.transform.y = self.y_bounds[1]

    def update(self):
        super(Character, self).update()
        self.transform.vel_y = self.fall_speed
        self.check_bounds()
        self.current.update()


