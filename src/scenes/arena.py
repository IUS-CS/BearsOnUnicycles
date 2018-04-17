# File: arena.py
# Authors: BearsOnUnicycles
# Since: 4/7/18
# This module is the main fighting arena for character objects -- Most of the game will be spent in this scene...
#       so don't f*** it up :)


from src import engine, input_handler as ih, game_objects

INPUT = ih.Handler()

CHARACTERS = {'Einstein': (game_objects.einstein, game_objects.einstein.Einstein),
              "Curie": (game_objects.curie, game_objects.curie.Curie),
              "NULL": None,
              }

P1_START_POS = (50, 0)
P2_START_POS = (400, 0)
BOUNDS = (960, 540)
COLLIDER_SIZE = (128, 128)

class Arena(engine.scene.Scene):

    player1 = None          # from game_objects.character.Character
    player2 = None
    UI = None               # from game_objects.UI.UI
    manager = None

    def __init__(self, manager, background, player1_name, player2_name, UI=False):
        super(Arena, self).__init__("arena", background, set_active=True)
        self.manager = manager
        self.player1 = CHARACTERS[player1_name][1](P1_START_POS,
                                                   COLLIDER_SIZE,
                                                   self.manager.physics.check_collisions)
        self.player1.name = "Player 1 ({})".format(player1_name)
        self.player2 = CHARACTERS[player2_name][1](P2_START_POS,
                                                   COLLIDER_SIZE,
                                                   self.manager.physics.check_collisions)
        self.player2.name = "Player 2 ({})".format(player2_name)
        self.player1.set_bounded(BOUNDS)
        self.player2.set_bounded(BOUNDS)
        if self.player1 is not None:
            self.add_game_object(self.player1)
            self.player1.input = player1_input
        if self.player2 is not None:
            self.add_game_object(self.player2)
            self.player2.input = player2_input
        if UI:
            self.add_game_object(game_objects.UI.UI(self.player1, self.player2))

    def flip_players(self):
        """orients the players transforms so
        that they will always face each other"""
        if self.player1 is not None and self.player2 is not None:
            if self.player1.transform.x < self.player2.transform.x:
                self.player1.transform.set_flip(False)
            else:
                self.player1.transform.set_flip(True)
            self.player2.transform.set_flip(not self.player1.transform.flip)

    def win_condition(self):
        """Checks to see if anyone won"""
        if self.player1.health <= 0:
            print("Player 1 Wins!")
            self.manager.change_to_active("Start Menu")
        if self.player2.health <= 0:
            print("Player 2 Wins!")
            self.manager.change_to_active("Start Menu")

    def update(self):
        self.flip_players()
        super(Arena, self).update()
        self.win_condition()



def get_input(player_num, input):
    """function that returns the input for each player"""
    controller_int = player_num - 1
    return INPUT.get_down("P{0}_{1}".format(player_num, input), controller_int)

def player1_input(input):
    """uses above to return input to player 1"""
    return get_input(1, input)

def player2_input(input):
    """uses above to return input to player 2"""
    return get_input(2, input)