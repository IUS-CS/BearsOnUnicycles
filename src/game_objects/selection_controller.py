
# File: selection_controller.py
# Authors: BearsOnUnicycles
# Since: 4/7/18
# This is the base class for all characters in the game and should be inherited from for each individual character


from src import engine


class State:

    title = ""
    next = None
    change = False
    frames = 0
    counter = 1

    def __init__(self, title, next, frames):
        self.title = title
        self.next = next
        self.frames = frames
        self.change = False
        self.counter = 1

    def set_next(self, next):
        self.next = next

    def update(self):
        if self.counter >= self.frames:
            self.change = True
        self.counter += 1


MAX_HEALTH = 100
LP_DAMAGE = 5
HP_DAMAGE = 10
LP_FRAMES = 2
HP_FRAMES = 4
BLOWBACK = 25  # pixels per frame


class SelectionControlller(engine.game_object.GameObject):

    transform = None
    animator = None
    collider = None
    x_bounds = ()
    y_bounds = ()
    input = None

    states = {}
    current = None
    next = None

    ignore_input = False  # ignore input until the state changes

    fall_speed = 25  # pixels per frame
    jump_frames = 10  # how long jump raises the character
    jump_counter = 1
    walk_speed = 10  # pixels per frame

    ignore_frames = 0
    ignore_frames_counter = 0

    grounded = False
    crouched = False
    walking = False
    jumping = True
    blocking = False
    attacking = False

    current_state = None

    def __init__(self, name, pos, size, collision_manager):
        super(SelectionControlller, self).__init__(name, set_active=True)
        self.size = size
        self.transform = t = engine.transform.Transform(pos[0], pos[1])
        self.add_component(t)
        self.animator = a = engine.animator.Animator()
        self.add_component(a)

        self.states = {}
        self.walking = False
        self.input = None
        self.ignore_frames = 0
        self.ignore_frames_counter = 0
        self.blocking = False
        self.attacking = False
        self.damage_output = 0
        self.attack_frames = 0
        self.attack_frames_counter = 0
        self.health = MAX_HEALTH

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
        if self.current is not None:
            self.current.counter = 1
            self.current.change = False
        self.current = self.states[state]
        self.next = self.states[self.current.next]
        self.animator.set_current(state)

    def get_state(self):
        return self.current_state

    def get_input(self, key):
        """returns the input callback passed
        from arena"""
        return self.input(key)

    def move(self, x_coord, y_coord):
        """moves the character from left to right"""
        # if right:
        #     self.transform.x += 75
        # elif left:
        #     self.transform.vel_x = -self.walk_speed
        # else:
        #     self.transform.vel_x = 0
        self.transform.x = x_coord
        self.transform.y = y_coord

    def state_machine(self):
        """
        precedence order is from bottom to top
        i.e. states at the bottom will override states
        at the top so be careful of the order"""
        # crouched
        # if self.crouched and not (self.current.title == "crouch_punch1" or self.current.title == "crouch_punch2"):
        #     self.change_state("crouch")
        #     self.move()
        if not self.crouched and self.walking and self.grounded:

            self.change_state("walk")

    def handle_inputs(self):
        """processes inputs for this object"""
        if self.input("RIGHT"):
            self.current_state = "RIGHT"
        elif self.input("LEFT"):
            self.current_state = "LEFT"
        elif self.input("ENTER"):
            self.current_state = "ENTER"
        else:
            self.current_state = "IDLE"

    def update(self):
        super(SelectionControlller, self).update()
        self.current.update()
        self.state_machine()
        if not self.ignore_input:
            self.handle_inputs()

        if self.current.change:
            self.change_state(self.next.title)


