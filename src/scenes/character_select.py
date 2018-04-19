# File: arena.py
# Authors: BearsOnUnicycles
# Since: 4/7/18
# This module is the main fighting arena for character objects -- Most of the game will be spent in this scene...
#       so don't f*** it up :)

import engine, input_handler as ih, game_objects, scenes

INPUT = ih.Handler()

BOXES = {'box1': (game_objects.selection_box, game_objects.selection_box.SelectionBox),
              "box2": (game_objects.selection_box, game_objects.selection_box.SelectionBox),
              "NULL": None,
              }
CHARACTERS = ["Curie", "Darwin", "Hawking", "Pythagoras", "Einstein", "Tesla", "Newton"]
POSITIONS = { "Curie": (52, 74), "Darwin": (262, 74), "Hawking": (472, 74), "Pythagoras": (687, 74),
              "Einstein": (159, 257), "Tesla": (370, 257), "Newton":(587, 257)}


P1_START_POS = (POSITIONS["Curie"][0], POSITIONS["Curie"][1])
P2_START_POS = (POSITIONS["Darwin"][0], POSITIONS["Darwin"][1])
BOUNDS = (960, 540)
COLLIDER_SIZE = (128, 128)


class CharacterSelect(engine.scene.Scene):

    player1 = None          # from game_objects.character.Character
    player2 = None
    manager = None
    current_char1 = 0
    current_char2 = 1
    enter_pressed = 0

    def __init__(self, manager, background, player1_name, player2_name):
        super(CharacterSelect, self).__init__("CharacterSelect", background, set_active=True)
        self.manager = manager
        self.player1 = BOXES[player1_name][1](P1_START_POS,
                                                   COLLIDER_SIZE,
                                                   self.manager.physics.check_collisions)

        self.player2 = BOXES[player2_name][1](P2_START_POS,
                                                   COLLIDER_SIZE,
                                                   self.manager.physics.check_collisions)

        if self.player1 is not None:
            self.add_game_object(self.player1)
            self.player1.input = player1_input
        if self.player2 is not None:
            self.add_game_object(self.player2)
            self.player2.input = player2_input

        self.player1.name = "Player 1 ({})".format(player1_name)
        self.player2.name = "Player 2 ({})".format(player2_name)

    def update_player1_current_selection_right(self):
        if self.current_char1 == 0:
            self.current_char1 += 1
            self.player1.move(POSITIONS["Darwin"][0], POSITIONS["Darwin"][1])
        elif self.current_char1 == 1:
            self.current_char1 += 1
            self.player1.move(POSITIONS["Hawking"][0], POSITIONS["Hawking"][1])
        elif self.current_char1 == 2:
            self.current_char1 += 1
            self.player1.move(POSITIONS["Pythagoras"][0], POSITIONS["Pythagoras"][1])
        elif self.current_char1 == 3:
            self.current_char1 += 1
            self.player1.move(POSITIONS["Einstein"][0], POSITIONS["Einstein"][1])
        elif self.current_char1 == 4:
            self.current_char1 += 1
            self.player1.move(POSITIONS["Tesla"][0], POSITIONS["Tesla"][1])
        elif self.current_char1 == 5:
            self.current_char1 += 1
            self.player1.move(POSITIONS["Newton"][0], POSITIONS["Newton"][1])
        elif self.current_char1 == 6:
            self.current_char1 = 0
            self.player1.move(POSITIONS["Curie"][0], POSITIONS["Curie"][1])

    def update_player1_current_selection_left(self):
        if self.current_char1 == 0:
            self.current_char1 = 6
            self.player1.move(POSITIONS["Newton"][0], POSITIONS["Newton"][1])
        elif self.current_char1 == 1:
            self.current_char1 -= 1
            self.player1.move(POSITIONS["Curie"][0], POSITIONS["Curie"][1])
        elif self.current_char1 == 2:
            self.current_char1 -= 1
            self.player1.move(POSITIONS["Darwin"][0], POSITIONS["Darwin"][1])
        elif self.current_char1 == 3:
            self.current_char1 -= 1
            self.player1.move(POSITIONS["Hawking"][0], POSITIONS["Hawking"][1])
        elif self.current_char1 == 4:
            self.current_char1 -= 1
            self.player1.move(POSITIONS["Pythagoras"][0], POSITIONS["Pythagoras"][1])
        elif self.current_char1 == 5:
            self.current_char1 -= 1
            self.player1.move(POSITIONS["Einstein"][0], POSITIONS["Einstein"][1])
        elif self.current_char1 == 6:
            self.current_char1 -= 1
            self.player1.move(POSITIONS["Tesla"][0], POSITIONS["Tesla"][1])

    def update_player2_current_selection_right(self):
        if self.current_char2 == 0:
            self.current_char2 += 1
            self.player2.move(POSITIONS["Darwin"][0], POSITIONS["Darwin"][1])
        elif self.current_char2 == 1:
            self.current_char2 += 1
            self.player2.move(POSITIONS["Hawking"][0], POSITIONS["Hawking"][1])
        elif self.current_char2 == 2:
            self.current_char2 += 1
            self.player2.move(POSITIONS["Pythagoras"][0], POSITIONS["Pythagoras"][1])
        elif self.current_char2 == 3:
            self.current_char2 += 1
            self.player2.move(POSITIONS["Einstein"][0], POSITIONS["Einstein"][1])
        elif self.current_char2 == 4:
            self.current_char2 += 1
            self.player2.move(POSITIONS["Tesla"][0], POSITIONS["Tesla"][1])
        elif self.current_char2 == 5:
            self.current_char2 += 1
            self.player2.move(POSITIONS["Newton"][0], POSITIONS["Newton"][1])
        elif self.current_char2 == 6:
            self.current_char2 = 0
            self.player2.move(POSITIONS["Curie"][0], POSITIONS["Curie"][1])

    def update_player2_current_selection_left(self):
        if self.current_char2 == 0:
            self.current_char2 = 6
            self.player2.move(POSITIONS["Newton"][0], POSITIONS["Newton"][1])
        elif self.current_char2 == 1:
            self.current_char2 -= 1
            self.player2.move(POSITIONS["Curie"][0], POSITIONS["Curie"][1])
        elif self.current_char2 == 2:
            self.current_char2 -= 1
            self.player2.move(POSITIONS["Darwin"][0], POSITIONS["Darwin"][1])
        elif self.current_char2 == 3:
            self.current_char2 -= 1
            self.player2.move(POSITIONS["Hawking"][0], POSITIONS["Hawking"][1])
        elif self.current_char2 == 4:
            self.current_char2 -= 1
            self.player2.move(POSITIONS["Pythagoras"][0], POSITIONS["Pythagoras"][1])
        elif self.current_char2 == 5:
            self.current_char2 -= 1
            self.player2.move(POSITIONS["Einstein"][0], POSITIONS["Einstein"][1])
        elif self.current_char2 == 6:
            self.current_char2 -= 1
            self.player2.move(POSITIONS["Tesla"][0], POSITIONS["Tesla"][1])

    def update(self):
        super(CharacterSelect, self).update()

        if self.player1.get_state() == "RIGHT":
            self.update_player1_current_selection_right()
        elif self.player1.get_state() == "LEFT":
            self.update_player1_current_selection_left()

        if self.player2.get_state() == "RIGHT":
            self.update_player2_current_selection_right()
        elif self.player2.get_state() == "LEFT":
            self.update_player2_current_selection_left()

        if self.player2.get_state() == "ENTER":
            self.enter_pressed +=1

        if self.player1.get_state() == "ENTER":
            self.enter_pressed +=1

        if (self.enter_pressed == 2):
            self.manager.add_scene(scenes.load_arena.LoadArena(self.manager, "/src/resources/levels/LondonAlley.jpg",
                                                               CHARACTERS[self.current_char1], CHARACTERS[self.current_char2], UI=True))
            self.manager.change_to_active("Load Arena")


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