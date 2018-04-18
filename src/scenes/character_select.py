# File: arena.py
# Authors: BearsOnUnicycles
# Since: 4/7/18
# This module is the main fighting arena for character objects -- Most of the game will be spent in this scene...
#       so don't f*** it up :)


from src import engine, input_handler as ih, game_objects

INPUT = ih.Handler()

SELECTIONS = {'box1': (game_objects.selection_box, game_objects.selection_box.SelectionBox),
              "box2": (game_objects.selection_box, game_objects.selection_box.SelectionBox),
              "NULL": None,
              }

BOX1_START = (50, 0)
BOX2_START = (400, 0)
BOX1 = "box1"
BOX2 = "box2"
SIZE = (118,118)

class CharacterSelect(engine.scene.Scene):

    player1 = None          # from game_objects.character.Character
    player2 = None
    UI = None               # from game_objects.UI.UI
    manager = None

    def __init__(self, manager, background):
        super(CharacterSelect, self).__init__("CharacterSelect", background, set_active=True)
        self.manager = manager
        self.player1 = SELECTIONS[BOX1][1](BOX1_START,
                                                   SIZE)

        self.player2 = SELECTIONS[BOX2][1](BOX2_START,
                                                   SIZE)
        if self.player1 is not None:
            self.add_game_object(self.player1)
            self.player1.input = player1_input
        if self.player2 is not None:
            self.add_game_object(self.player2)
            self.player2.input = player2_input

        self.player1.name = "Player 1 ({})".format(BOX1)
        self.player2.name = "Player 2 ({})".format(BOX2)

    def update(self):
        super(CharacterSelect, self).update()



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