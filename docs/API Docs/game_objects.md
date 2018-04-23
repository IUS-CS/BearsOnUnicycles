game\_objects package
=========================



Submodules
----------


game\_objects.UI module
---------------------------

- This module controls the user interface for the arena

		class UI(engine.game_object.GameObject):
			- Class that handles displaying the UI for each character in the arena
		
		def __init__(self, player1, player2):
		
		def update(self):

game\_objects.character module
----------------------------------
- This is the base class for all characters in the game and should be inherited from for each individual character

	
		class State:

    		def set_next(self, next):
    			- Sets next state

    		def update(self):
    			

		class Character(engine.game_object.GameObject):
		
			def load_animations(self, anim_list):
				- Loads all a characters animations based of the values in anim_list must include an animation called 'idle'

        	format for animation loading is:
        		(title,       # the title of the animation
        		start,       # the starting (x, y) in pixels
        		count,       # the number of frames
        		size,        # the pixel size of each frame
        		path,        # the path to the sprite sheet
        		sheet_size,  # the dimensions of the sprite sheet
        priority)

    		def load_states(self, states):
    			- Loads states into the charcaters state machine
        
			def change_state(self, state):
				- changes the current state to #state

    		def set_bounded(self, screen):
    			- Ensures character stays on screen

    		def check_bounds(self):
    			- adheres the object to its borders

    		def get_input(self, key):
    			- returns the input callback passed from arena
    
    		def jump(self):
    			- jumps the character using transform.vel_y

    		def move(self, right=False, left=False):
    			- moves the character from left to right

    		def state_machine(self):
    			- precedence order is from bottom to top
    			- i.e. states at the bottom will override states at the top so be careful of the order

    		def handle_inputs(self):
    			- processes inputs for this object

    		def ignore_input_timer(self, frames):
    			- Ignores controller input for a certain amount of time in frames

    		def check_ignore(self):
    			- set the ignore_input bool

    		def attack(self, frames):
    			- Sets the attacking bool true for so many frames

			def check_attack(self):
				- Checks to see if the attacking bool should be cleared
        

    		def damage(self, amount):
    			- Deals damage to the character

    		def blowback_timer(self, frames):
        		- sets blowback to true for a certain amount of frames
        
    		def check_blown(self):
    			- clears the blowback bool if needed

    		def blowback(self):
    			- moves the player away from the damage on a successful hit
        
			def on_collision(self):
				- Handles the logic of collisions for damage calculations
		
		 def update(self):
    	
game\_objects.curie module
------------------------------
- This module defines the fighter Marie Curie and defines her animations and logic

		format for animation loading is:
        (title,       # the title of the animation
        start,       # the starting (x, y) in pixels
        count,       # the number of frames
        size,        # the pixel size of each frame
        path,        # the path to the sprite sheet
        sheet_size,  # the dimensions of the sprite sheet
        priority)

		class Curie(character.Character):
			- Instantiates the Curie character, and initializes the animations and states

		def __init__(self, pos, size, collision_manager):

    	def update(self):

game\_objects.darwin module
-------------------------------
- This module defines the character Darwin including his animations and logic

		format for animation loading is:
        (title,       # the title of the animation
        start,       # the starting (x, y) in pixels
        count,       # the number of frames
        size,        # the pixel size of each frame
        path,        # the path to the sprite sheet
        sheet_size,  # the dimensions of the sprite sheet
        priority)

		class Darwin(character.Character):
			- Instantiates the Darwin character, and initializes the animations and states
    
    	def __init__(self, pos, size, collision_manager):
    	
    	def update(self):


game\_objects.einstein module
---------------------------------
- This module defines the character Albert Einstein's animations, logic

		format for animation loading is:
        (title,       # the title of the animation
        start,       # the starting (x, y) in pixels
        count,       # the number of frames
        size,        # the pixel size of each frame
        path,        # the path to the sprite sheet
        sheet_size,  # the dimensions of the sprite sheet
        priority)

		class Einstein(character.Character):
			- Instantiates the Newton character, and initializes the animations and states
    
    	def __init__(self, pos, size, collision_manager):

    	def update(self):
        
game\_objects.hawking module
--------------------------------
- This module defines the character Hawking including his animations and logic

			format for animation loading is:
        	(title,       # the title of the animation
        	start,       # the starting (x, y) in pixels
        	count,       # the number of frames
        	size,        # the pixel size of each frame
        	path,        # the path to the sprite sheet
        	sheet_size,  # the dimensions of the sprite sheet
        	priority)
        	
        	
        	class Hawking(character.Character):
    			- Instantiates the Newton character, and initializes the animations and states

    	def __init__(self, pos, size, collision_manager):
    	
    	def set_bounded(self, screen):

    	def update(self):

game\_objects.health\_bar module
------------------------------------
- This module defines the logic for the health bar for each character

		class HealthBar(engine.game_object.GameObject):
		    - Instantiates the health bars for each character, and initializes them to be used in the arena

    	def __init__(self, character, player1=False, player2=False):

    	def update(self):


game\_objects.nametag module
--------------------------------

- This module displays a nametag in the arena scene

		class Nametag(engine.game_object.GameObject):
			- Instantiates the nametags for each character, and initializes them to be used in the arena

		def __init__(self, player, key):

    	def update(self):

game\_objects.newton module
-------------------------------
- This module defines the character newton including his animations and logic
			
		format for animation loading is:
		(title,       # the title of the animation
		start,       # the starting (x, y) in pixels
		count,       # the number of frames
		size,        # the pixel size of each frame
		path,        # the path to the sprite sheet
		sheet_size,  # the dimensions of the sprite sheet
		priority)
		
		class Newton(character.Character):
        	    - Instantiates the Newton character, and initializes the animations and states

		def __init__(self, pos, size, collision_manager):
        
    	def set_bounded(self, screen):
        
    	def update(self):
    	

game\_objects.pythagoras module
-----------------------------------

- This module defines the character Albert Pythagoras's animations, logic

		format for animation loading is:
		(title,       # the title of the animation
		start,       # the starting (x, y) in pixels
		count,       # the number of frames
		size,        # the pixel size of each frame
		path,        # the path to the sprite sheet
		sheet_size,  # the dimensions of the sprite sheet
		priority)
		
		class Pythagoras(character.Character):
        	    - Instantiates the Pythagoras character, and initializes the animations and states

		def __init__(self, pos, size, collision_manager):
        
    	def set_bounded(self, screen):
        
    	def update(self):


game\_objects.selection\_box module
---------------------------------------

- This module defines the character selection box logic

		format for animation loading is:
		(title,       # the title of the animation
		start,       # the starting (x, y) in pixels
		count,       # the number of frames
		size,        # the pixel size of each frame
		path,        # the path to the sprite sheet
		sheet_size,  # the dimensions of the sprite sheet
		priority)
		
		class SelectionBox(character.Character):
			- Instantiates the Newton character, and initializes the animations and states

		def __init__(self, pos, size, player2=False):        
    	
    	def set_bounded(self, screen):
        
    	def update(self):


game\_objects.selection\_controller module
----------------------------------------------

- This is the base class for the selection boxes


		class State:
			- Handles the states of the selection box, and keeps track of which states are active
		
    
    	def __init__(self, title, next, frames):
        
    	def set_next(self, next):

    	def update(self):
    	
    	class SelectionControlller(engine.game_object.GameObject):

    	def __init__(self, name, pos, size):

    	def load_animations(self, anim_list):
    		- Loads all a characters animations based of the values in anim_list must include an animation called ' idle'

        format for animation loading is:
        (title,       # the title of the animation
        start,       # the starting (x, y) in pixels
        count,       # the number of frames
        size,        # the pixel size of each frame
        path,        # the path to the sprite sheet
        sheet_size,  # the dimensions of the sprite sheet
        priority)

    	def load_states(self, states):
        	- Loads states into the charcaters
        state machine

    	def change_state(self, state):
    		- changes the current state to
        #state

    	def get_state(self):
    		- returns the current active	state

    	def get_input(self, key):
        	- returns the input callback passed from character select screen

    	def move(self, x_coord, y_coord):
    		- moves the selection box from left to right
    		
    	def handle_inputs(self):
    		- processes inputs for this object

    	def update(self):
    	

game\_objects.tesla module
------------------------------
- this file defines the character Albert tesla's animations, logic

		format for animation loading is:
		(title,       # the title of the animation
		start,       # the starting (x, y) in pixels
		count,       # the number of frames
		size,        # the pixel size of each frame
		path,        # the path to the sprite sheet
		sheet_size,  # the dimensions of the sprite sheet
		priority)

		class Tesla(character.Character):
    		- Instantiates the Telsa character, and initializes the animations and states

    	def __init__(self, pos, size, collision_manager):

    	def update(self):
      