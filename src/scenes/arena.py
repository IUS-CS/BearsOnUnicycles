# File: arena.py
# Authors: BearsOnUnicycles
# Since: 4/7/18
# This module is the main fighting arena for character objects -- Most of the game will be spent in this scene...
#       so don't f*** it up :)


from src import engine, input_handler as ih

INPUT = ih.Handler()


class Arena(engine.scene.Scene):

    player1 = None          # from game_objects.character.Character
    player2 = None
    UI = None               # from game_objects.UI.UI
    manager = None

    def __init__(self, manager, background, player1, player2, UI):
        super(Arena, self).__init__("arena", background, set_active=True)
        self.manager = manager
        self.player1 = player1
        self.player2 = player2
        if player1 is not None:
            self.add_game_object(player1)
            player1.input = player1_input
        if player2 is not None:
            self.add_game_object(player2)
            player2.input = player2_input
        self.UI = UI
        if UI is not None:
            self.add_game_object(UI)

    def flip_players(self):
        """orients the players transforms so
        that they will always face each other"""
        if self.player1 is not None and self.player2 is not None:
            if self.player1.transform.x < self.player2.transform.x:
                self.player1.transform.set_flip(False)
            else:
                self.player1.transform.set_flip(True)
            self.player2.transform.set_flip(not self.player1.transform.flip)

    def update(self):
        self.flip_players()
        super(Arena, self).update()



def get_input(player_num, input):
    """function that returns the input for each player"""
    return INPUT.get_down("P{0}_{1}".format(player_num, input))

def player1_input(input):
    """uses above to return input to player 1"""
    return get_input(1, input)

def player2_input(input):
    """uses above to return input to player 2"""
    return get_input(2, input)