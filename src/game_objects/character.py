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


class Character(engine.game_object.GameObject):

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
    blown = False
    blown_frames = 0
    blown_frames_counter = 0
    damage_output = 0

    vulnerable_modifier = 4  # adds frames to an action to make the player vulnerable

    health = 0

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
        self.grounded = False
        self.crouched = False
        self.jumping = False
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

    def set_bounded(self, screen):
        """Ensures character stays on screen"""
        self.x_bounds = (-screen[0] / 2 + self.size[0] * 3, screen[0] / 2 + self.size[0])
        self.y_bounds = (-screen[1] / 2 + self.size[1] * .3, screen[1] / 2 - screen[1] * .3)

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

    def get_input(self, key):
        """returns the input callback passed
        from arena"""
        return self.input(key)

    def jump(self):
        """jumps the character using transform.vel_y"""
        if self.jump_counter < self.jump_frames:
            self.transform.vel_y = -self.fall_speed
            self.jump_counter += 1
        else:
            self.jump_counter = 0
            self.transform.vel_y = self.fall_speed
            self.jumping = False

    def move(self, right=False, left=False):
        """moves the character from left to right"""
        if right:
            self.transform.vel_x = self.walk_speed
        elif left:
            self.transform.vel_x = -self.walk_speed
        else:
            self.transform.vel_x = 0

    def state_machine(self):
        """
        precedence order is from bottom to top
        i.e. states at the bottom will override states
        at the top so be careful of the order"""
        if not self.grounded:
            # landing
            if self.transform.y >= self.y_bounds[1]:
                self.change_state("idle")
                self.grounded = True
        else:
            # jumping
            if self.transform.y < self.y_bounds[1]:
                self.change_state('jump')
                self.grounded = False
        # crouched
        if self.crouched and not (self.current.title == "crouch_punch1" or self.current.title == "crouch_punch2"):
            self.change_state("crouch")
            self.move()
        if not self.crouched and self.walking and self.grounded:
            self.change_state("walk")

    def handle_inputs(self):
        """processes inputs for this object"""
        if self.input("UP") and self.grounded:
            self.jumping = True
        if self.input("DOWN") and self.grounded:
            self.crouched = True
        else:
            self.crouched = False
        if not self.crouched:
            if self.input("RIGHT") or self.input("LEFT") and self.grounded:
                self.walking = True
            else:
                self.walking = False
            if self.input("RIGHT"):
                self.move(right=True)
                if self.transform.flip:
                    self.blocking = True
                else:
                    self.blocking = False
            elif self.input("LEFT"):
                if not self.transform.flip:
                    self.blocking = True
                else:
                    self.blocking = False
                self.move(left=True)
            else:
                self.move()
                self.blocking = False
        # air punches
        if not self.grounded:
            if self.input("LIGHT_PUNCH"):
                self.change_state("air_punch1")
                self.ignore_input_timer(self.states["air_punch1"].frames)
                self.attack(LP_FRAMES)
                self.damage_output = LP_DAMAGE
            elif self.input("HEAVY_PUNCH"):
                self.change_state("air_punch2")
                self.ignore_input_timer(self.states["air_punch2"].frames)
                self.attack(HP_FRAMES)
                self.damage_output = HP_DAMAGE
        # regular punches
        if self.grounded and not self.crouched:
            if self.input("LIGHT_PUNCH"):
                self.change_state("punch1")
                self.ignore_input_timer(self.states["punch1"].frames)
                self.attack(LP_FRAMES)
                self.damage_output = LP_DAMAGE
            elif self.input("HEAVY_PUNCH"):
                self.change_state("punch2")
                self.ignore_input_timer(self.states["punch2"].frames)
                self.attack(HP_FRAMES)
                self.damage_output = HP_DAMAGE
        # crouch punches
        if self.crouched:
            if self.input("LIGHT_PUNCH"):
                self.change_state("crouch_punch1")
                self.ignore_input_timer(self.states["crouch_punch1"].frames)
                self.attack(LP_FRAMES)
                self.damage_output = LP_DAMAGE
            elif self.input("HEAVY_PUNCH"):
                self.change_state("crouch_punch2")
                self.ignore_input_timer(self.states["crouch_punch2"].frames)
                self.attack(HP_FRAMES)
                self.damage_output = HP_DAMAGE

    def ignore_input_timer(self, frames):
        """Ignores controller input for a certain
        amount of time in frames"""
        self.ignore_frames = frames + self.vulnerable_modifier
        self.ignore_frames_counter = 1

    def check_ignore(self):
        """set the ignore_input bool"""
        if self.ignore_frames:
            self.ignore_frames_counter += 1
            if self.ignore_frames_counter >= self.ignore_frames:
                self.ignore_input = False
            else:
                self.ignore_input = True

    def attack(self, frames):
        """Sets the attacking bool true
        for so many frames"""
        if not self.attacking:
            self.attacking = True
            self.attack_frames = frames
            self.attack_frames_counter = 0

    def check_attack(self):
        """Checks to see if the
        attacking bool should be cleared"""
        if self.attacking:
            self.attack_frames_counter += 1
            if self.attack_frames_counter >= self.attack_frames:
                self.attacking = False
            else:
                self.attacking = True

    def damage(self, amount):
        """Deals damage to the character"""
        if self.health > 0:
            self.health -= amount
        self.blowback_timer(amount / 2)
        print(self.name, self.health)

    def blowback_timer(self, frames):
        """sets blowback to true for
        a certain amount of frames"""
        self.blown = True
        self.blown_frames = frames
        self.blown_frames_counter = 1

    def check_blown(self):
        """clears the blowback bool
        if needed"""
        if self.blown:
            self.blown_frames_counter += 1
            if self.blown_frames_counter >= self.blown_frames:
                self.blown = False
            else:
                self.blown = True

    def blowback(self):
        """moves the player away from the
        damage on a successful hit"""
        if self.blown:
            if self.transform.flip:
                self.transform.vel_x = BLOWBACK
            else:
                self.transform.vel_x = -BLOWBACK

    def on_collision(self):
        """Handles the logic of
        collisions for damage calculations"""
        # if we make contact with another player
        for g in self.collider.collisions:
            if g[1] != self.name:
                # if they are attacking and we are not blocking (walking backwards)
                if self.scene.get_object_by_name(g[1]).attacking and not self.blocking:
                    self.damage(self.scene.get_object_by_name(g[1]).damage_output)

    def update(self):
        super(Character, self).update()
        self.transform.vel_y = self.fall_speed
        self.check_bounds()
        self.current.update()
        if self.jumping:
            self.jump()
        self.state_machine()
        if not self.ignore_input:
            self.handle_inputs()
        else:
            self.move()  # fix for sliding bug
        if self.current.change:
            self.change_state(self.next.title)
        self.check_ignore()
        if self.collider.colliding:
            self.on_collision()
        if not self.attacking:
            self.damage_output = 0
        self.check_attack()
        self.check_blown()
        self.blowback()

