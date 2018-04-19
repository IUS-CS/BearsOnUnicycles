# File: character_select.py
# Authors: BearsOnUnicycles
# Since: 4/18/18
# This module handles the character selection screen, and once both players have select
# it then loads the arena with the chosen characters

from src import engine, input_handler as ih, game_objects, scenes

INPUT = ih.Handler()

BOXES = {'box1': (game_objects.selection_box, game_objects.selection_box.SelectionBox),
              "box2": (game_objects.selection_box, game_objects.selection_box.SelectionBox),
              "NULL": None,
              }
CHARACTERS = ["Curie", "Darwin", "Hawking", "Pythagoras", "Einstein", "Tesla", "Newton"]
POSITIONS = { "Curie": (47, 70), "Darwin": (269, 70), "Hawking": (493, 70), "Pythagoras": (725, 72),
              "Einstein": (159, 267), "Tesla": (383, 267), "Newton": (613, 265)}


BOX1_START = (POSITIONS["Curie"][0], POSITIONS["Curie"][1])
BOX2_START = (POSITIONS["Darwin"][0], POSITIONS["Darwin"][1])
SIZE = (128, 128)


class CharacterSelect(engine.scene.Scene):

    box1 = None
    box2 = None
    manager = None
    current_char1 = 0
    current_char2 = 1
    enter_pressed = 0

    def __init__(self, manager, background, box1_name, box2_name):
        super(CharacterSelect, self).__init__("CharacterSelect", background, set_active=True)
        self.manager = manager
        self.box1 = BOXES[box1_name][1](BOX1_START, SIZE)
        self.box2 = BOXES[box2_name][1](BOX2_START, SIZE, player2=True)

        if self.box2 is not None:
            self.add_game_object(self.box1)
            self.box1.input = box1_input
        if self.box2 is not None:
            self.add_game_object(self.box2)
            self.box2.input = box2_input

        self.box1.name = "Player 1 ({})".format(box1_name)
        self.box2.name = "Player 2 ({})".format(box2_name)

        player1_name = engine.game_object.GameObject("P1_name", set_active=True)
        player1_name.add_component(engine.transform.Transform(x=25, y=450))
      #  player1_name.add_component(engine.sprite.Sprite("/src/resources/misc/player1_name.png", (0, 0), (300, 50), 1))
        self.add_game_object(player1_name)

        player2_name = engine.game_object.GameObject("P2_name", set_active=True)
        player2_name.add_component(engine.transform.Transform(x=600, y=450))
       # player2_name.add_component(engine.sprite.Sprite("/src/resources/misc/player2_name.png", (0, 0), (300, 50), 1))
        self.add_game_object(player2_name)

        choose = engine.game_object.GameObject("Choose", set_active=True)
        choose.add_component(engine.transform.Transform(x=175))
        #choose.add_component(engine.sprite.Sprite("/src/resources/misc/choose.png", (0, 0), (600, 100), 1))
        self.add_game_object(choose)

    def update_box1_current_selection_right(self):
        if self.current_char1 == 0:
            self.current_char1 += 1
            self.box1.move(POSITIONS["Darwin"][0], POSITIONS["Darwin"][1])
        elif self.current_char1 == 1:
            self.current_char1 += 1
            self.box1.move(POSITIONS["Hawking"][0], POSITIONS["Hawking"][1])
        elif self.current_char1 == 2:
            self.current_char1 += 1
            self.box1.move(POSITIONS["Pythagoras"][0], POSITIONS["Pythagoras"][1])
        elif self.current_char1 == 3:
            self.current_char1 += 1
            self.box1.move(POSITIONS["Einstein"][0], POSITIONS["Einstein"][1])
        elif self.current_char1 == 4:
            self.current_char1 += 1
            self.box1.move(POSITIONS["Tesla"][0], POSITIONS["Tesla"][1])
        elif self.current_char1 == 5:
            self.current_char1 += 1
            self.box1.move(POSITIONS["Newton"][0], POSITIONS["Newton"][1])
        elif self.current_char1 == 6:
            self.current_char1 = 0
            self.box1.move(POSITIONS["Curie"][0], POSITIONS["Curie"][1])

    def update_box1_current_selection_left(self):
        if self.current_char1 == 0:
            self.current_char1 = 6
            self.box1.move(POSITIONS["Newton"][0], POSITIONS["Newton"][1])
        elif self.current_char1 == 1:
            self.current_char1 -= 1
            self.box1.move(POSITIONS["Curie"][0], POSITIONS["Curie"][1])
        elif self.current_char1 == 2:
            self.current_char1 -= 1
            self.box1.move(POSITIONS["Darwin"][0], POSITIONS["Darwin"][1])
        elif self.current_char1 == 3:
            self.current_char1 -= 1
            self.box1.move(POSITIONS["Hawking"][0], POSITIONS["Hawking"][1])
        elif self.current_char1 == 4:
            self.current_char1 -= 1
            self.box1.move(POSITIONS["Pythagoras"][0], POSITIONS["Pythagoras"][1])
        elif self.current_char1 == 5:
            self.current_char1 -= 1
            self.box1.move(POSITIONS["Einstein"][0], POSITIONS["Einstein"][1])
        elif self.current_char1 == 6:
            self.current_char1 -= 1
            self.box1.move(POSITIONS["Tesla"][0], POSITIONS["Tesla"][1])

    def update_box2_current_selection_right(self):
        if self.current_char2 == 0:
            self.current_char2 += 1
            self.box2.move(POSITIONS["Darwin"][0], POSITIONS["Darwin"][1])
        elif self.current_char2 == 1:
            self.current_char2 += 1
            self.box2.move(POSITIONS["Hawking"][0], POSITIONS["Hawking"][1])
        elif self.current_char2 == 2:
            self.current_char2 += 1
            self.box2.move(POSITIONS["Pythagoras"][0], POSITIONS["Pythagoras"][1])
        elif self.current_char2 == 3:
            self.current_char2 += 1
            self.box2.move(POSITIONS["Einstein"][0], POSITIONS["Einstein"][1])
        elif self.current_char2 == 4:
            self.current_char2 += 1
            self.box2.move(POSITIONS["Tesla"][0], POSITIONS["Tesla"][1])
        elif self.current_char2 == 5:
            self.current_char2 += 1
            self.box2.move(POSITIONS["Newton"][0], POSITIONS["Newton"][1])
        elif self.current_char2 == 6:
            self.current_char2 = 0
            self.box2.move(POSITIONS["Curie"][0], POSITIONS["Curie"][1])

    def update_box2_current_selection_left(self):
        if self.current_char2 == 0:
            self.current_char2 = 6
            self.box2.move(POSITIONS["Newton"][0], POSITIONS["Newton"][1])
        elif self.current_char2 == 1:
            self.current_char2 -= 1
            self.box2.move(POSITIONS["Curie"][0], POSITIONS["Curie"][1])
        elif self.current_char2 == 2:
            self.current_char2 -= 1
            self.box2.move(POSITIONS["Darwin"][0], POSITIONS["Darwin"][1])
        elif self.current_char2 == 3:
            self.current_char2 -= 1
            self.box2.move(POSITIONS["Hawking"][0], POSITIONS["Hawking"][1])
        elif self.current_char2 == 4:
            self.current_char2 -= 1
            self.box2.move(POSITIONS["Pythagoras"][0], POSITIONS["Pythagoras"][1])
        elif self.current_char2 == 5:
            self.current_char2 -= 1
            self.box2.move(POSITIONS["Einstein"][0], POSITIONS["Einstein"][1])
        elif self.current_char2 == 6:
            self.current_char2 -= 1
            self.box2.move(POSITIONS["Tesla"][0], POSITIONS["Tesla"][1])

    def update(self):
        super(CharacterSelect, self).update()

        if self.box1.get_state() == "RIGHT":
            self.update_box1_current_selection_right()

        elif self.box1.get_state() == "LEFT":
            self.update_box1_current_selection_left()

        if self.box2.get_state() == "RIGHT":
            self.update_box2_current_selection_right()

        elif self.box2.get_state() == "LEFT":
            self.update_box2_current_selection_left()

        if self.box1.get_state() == "ENTER":
            self.enter_pressed +=1

        if self.box2.get_state() == "ENTER":
            self.enter_pressed +=1

        if self.enter_pressed == 2:
            self.manager.add_scene(scenes.load_arena.LoadArena(self.manager,
                                                               "/src/resources/levels/LondonAlley.jpg",
                                                               CHARACTERS[self.current_char1],
                                                               CHARACTERS[self.current_char2],
                                                               UI=True))
            self.manager.change_to_active("Load Arena")


def get_input(player_num, input):
    """function that returns the input for each player"""
    controller_int = player_num - 1
    return INPUT.get_down("P{0}_{1}".format(player_num, input), controller_int)


def box1_input(input):
    """uses above to return input to player 1"""
    return get_input(1, input)


def box2_input(input):
    """uses above to return input to player 2"""
    return get_input(2, input)