Scenes package
-------------------

Submodules
----------

scenes.arena module
-----------------------
- This module is the main fighting arena for character objects -- Most of the game will be spent in this scene...


		CHARACTERS = {'Einstein': (game_objects.einstein, game_objects.einstein.Einstein),
              "Curie": (game_objects.curie, game_objects.curie.Curie),
              "Darwin": (game_objects.darwin, game_objects.darwin.Darwin),
              "Hawking": (game_objects.hawking, game_objects.hawking.Hawking),
              "Newton": (game_objects.newton, game_objects.newton.Newton),
              "Pythagoras": (game_objects.pythagoras, game_objects.pythagoras.Pythagoras),
              "Tesla": (game_objects.tesla, game_objects.tesla.Tesla),
              "NULL": None,
              }

		Arena(engine.scene.Scene):
    		- This is the class for the actual fighting arena of the game. Handlesthe logic and input of each character, then calls the appropriate win screen to re-loop the game
       
		def flip_players(self):
        	- Orients the players transforms so
        that they will always face each other

		def win_condition(self):
			- Checks to see if anyone won

    	def update(self):

		def get_input(player_num, input):
    		- function that returns the input for each player
    	
		def player1_input(input):
    		- uses above to return input to player 1

		def player2_input(input):
    		- uses above to return input to player 2

scenes.character\_select module
-----------------------------------
- This module handles the character selection screen, and once both players have select it then loads the arena with the chosen characters


		class CharacterSelect(engine.scene.Scene):
			- The character select class controls the character select screen, and handles keeping track of player input, returning the character they selected
    

    	def update_box1_current_selection_right(self):
			- Updates the current location of player 1's box if they move in the right direction
        
    	def update_box1_current_selection_left(self):
    		- Updates the current location of player 1's box if they move in the left direction

    	def update_box2_current_selection_right(self):
			- Updates the current location of player 2's box if they move in the right direction

    	def update_box2_current_selection_left(self):
    		- Updates the current location of player 2's box if they move in the left direction
        
    	def update(self):
    		- Updates the entire scene and checks for player input, calling the appropriate update position, or updating the counter to know when both players press enter.

		def get_input(player_num, input):
    		- function that returns the input for each player

		def box1_input(input):
		   	- uses above to return input to player 1
    
		def box2_input(input):
    		- uses above to return input to player 2

scenes.load\_arena module
-----------------------------
- This is the loading screen for the arena

		class LoadArena(engine.scene.Scene):
		   - Displays animated loading screen while assets and characters load

    	def update(self):
	       - Updates the entire screen
        and switches to the arena when loading is done	        
  
scenes.splash module
------------------------

- This file displays the splash screen and plays the splash sound

		class Splash(engine.scene.Scene):
    		- Handles the opening splash screen and sound
		def update(self):
			- Updates the entire screen, then loads the start menu


scenes.start\_menu module
-----------------------------

- This file creates the start menu scene, a simple title screen where the user must press a button to continue

		
		class StartMenu(engine.scene.Scene):
			- Handles the start menu, checks for input, then loads the character selection screen

    	def update(self):
    		- Updates screen and checks for input pressed,
        then switches to the Character Selection screen
        

scenes.win\_screen module
-----------------------------

- This module displays the screen after a player has won in Arena

		class WinScreen(engine.scene.Scene):
			- Handles the screen played once a player wins

    	def update(self):
    		- Updates and displays the win screen, then reloads the start menu
       