# File: input_handler.py
# Authors: BearsOnUnicycles
# Since: 3/10/18
# this file handles all the input from the keyboard
import pygame as pg


class ButtonMap:
    game_pad_present = False  # determines which map to use for input
    game_pads = []  # holds configuration for each game pad/ joystick

    # holds the button mapping to pygame events regardless of whether via keyboard or game pad
    input = {"P1_RIGHT",
             "P1_LEFT",
             "P1_UP",
             "P1_DOWN",
             "P1_LIGHT_PUNCH",
             "P1_MID_PUNCH",
             "P1_HEAVY_PUNCH",
             "P1_LIGHT_KICK",
             "P1_MID_KICK",
             "P1_HEAVY_KICK",
             "P1_ENTER"
             }

    # each pg.K_ value corrisponds to an index in the matrix returned by the function pg.key.get_pressed
    keyboard_map = {"P1_RIGHT": pg.K_d,
                    "P1_LEFT": pg.K_a,
                    "P1_UP": pg.K_w,
                    "P1_DOWN": pg.K_s,
                    "P1_LIGHT_PUNCH": pg.K_u,
                    "P1_MID_PUNCH": pg.K_i,
                    "P1_HEAVY_PUNCH": pg.K_o,
                    "P1_LIGHT_KICK": pg.K_j,
                    "P1_MID_KICK": pg.K_k,
                    "P1_HEAVY_KICK": pg.K_l,
                    "P1_ENTER": pg.K_t,

                    "P2_RIGHT": pg.K_RIGHT,
                    "P2_LEFT": pg.K_LEFT,
                    "P2_UP": pg.K_UP,
                    "P2_DOWN": pg.K_DOWN,
                    "P2_LIGHT_PUNCH": pg.K_q,
                    "P2_MID_PUNCH": pg.K_q,
                    "P2_HEAVY_PUNCH": pg.K_q,
                    "P2_LIGHT_KICK": pg.K_q,
                    "P2_MID_KICK": pg.K_q,
                    "P2_HEAVY_KICK": pg.K_q,
                    "P2_ENTER": pg.K_RETURN

                    }
    joystick_map= {"P1_RIGHT": "P1_RIGHT",
                             "P1_LEFT": "P1_LEFT",
                             "P1_UP": "P1_UP",
                             "P1_DOWN": "P1_DOWN",
                             "P1_LIGHT_PUNCH": 4,
                             "P1_MID_PUNCH": 0,
                             "P1_HEAVY_PUNCH": 3,
                             "P1_LIGHT_KICK": 6,
                             "P1_MID_KICK": 1,
                             "P1_HEAVY_KICK": 2,
                             "P1_ENTER": 9,

                             "P2_RIGHT": "P2_RIGHT",
                             "P2_LEFT": "P2_LEFT",
                             "P2_UP": "P2_UP",
                             "P2_DOWN": "P2_DOWN",
                             "P2_LIGHT_PUNCH": 4,
                             "P2_MID_PUNCH": 0,
                             "P2_HEAVY_PUNCH": 3,
                             "P2_LIGHT_KICK": 6,
                             "P2_MID_KICK": 1,
                             "P2_HEAVY_KICK": 2,
                             "P2_ENTER": 9,
                             }


    joystick_hat_conversion_map_0 = {"P1_RIGHT": (0, 1),
                                   "P1_LEFT": (0, -1),
                                   "P1_UP": (1, 1),
                                   "P1_DOWN": (1, -1),
                                     }

    joystick_hat_conversion_map_1 = {"P2_RIGHT": (0, 1),
                                   "P2_LEFT": (0, -1),
                                   "P2_UP": (1, 1),
                                   "P2_DOWN": (1, -1)

                                   }

    def get_hat_direction(self, button):
        direction_check = self.joystick_hat_conversion_map[button][0]
        going_that_way_check = self.joystick_hat_conversion_map[button][1]
        actual_input = self.game_pads[0].get_hat(0)[direction_check]

        if actual_input == going_that_way_check:
            return 1
        else:
            return 0

    def get_down_keyboard(self, key):
        """Using the pygame function to get input. All keys are returned by get_pressed.
        We only want the ones we have mapped above so we feed in the index in question to get back what we want
        """

        return pg.key.get_pressed()[key]

    def get_down_gamepad(self, key, controller):

        if (key in self.joystick_hat_conversion_map_0.keys() or key in self.joystick_hat_conversion_map_1.keys()):
            direction_check = None
            actual_input = None
            going_that_way_check = None

            if key in self.joystick_hat_conversion_map_0.keys() and controller == 0:
                direction_check = self.joystick_hat_conversion_map_0[key][0]
                actual_input = self.game_pads[0].get_hat(0)[direction_check]
                going_that_way_check = self.joystick_hat_conversion_map_0[key][1]
            if (key in self.joystick_hat_conversion_map_1.keys() and controller == 1):
                direction_check = self.joystick_hat_conversion_map_1[key][0]
                actual_input = self.game_pads[1].get_hat(0)[direction_check]
                going_that_way_check = self.joystick_hat_conversion_map_1[key][1]

            if actual_input == going_that_way_check: return 1
            else: return 0

        else:
            return self.game_pads[controller].get_button(key)


    """detect how many controllers are connected,
        determine which mapping to use,
        initialize each controller,
        display the name of that controller
    """

    def set_gamepads(self):
        pg.joystick.init()  # must be done before other joystick functions work
        joystick_count = pg.joystick.get_count()

        if joystick_count == 2:
            self.game_pad_present = True  

            print(joystick_count, "game pad(s) detected")
            for i in range((joystick_count)):
                # add controller to joystick list
                self.game_pads.append(pg.joystick.Joystick(i))
                self.game_pads[i].init()  # must be initialized in the list
                print(".Game pad detected: {} assigned to player {}".format(self.game_pads[i].get_name(), (i + 1)))
                print(self.game_pads[i].get_numbuttons(), "buttons detected on joystick", i)
                i = i + 1
        else:
            print("Not two joysticks?!  SHAME ON YOU")
            print("use the keyboard")
    def __init__(self):

        self.set_gamepads()




class Handler:
    class __Handler:  # this bit makes it a singleton

        bmap = ButtonMap()
        keys = bmap.input

        def __init__(self):

            self.p1_keys = {"P1_RIGHT": False,
                         "P1_LEFT": False,
                         "P1_UP": False,
                         "P1_DOWN": False,
                         "P1_LIGHT_PUNCH": False,
                         "P1_MID_PUNCH": False,
                         "P1_HEAVY_PUNCH": False,
                         "P1_LIGHT_KICK": False,
                         "P1_MID_KICK": False,
                         "P1_HEAVY_KICK": False,
                         'P1_ENTER': False,
                            }

            self.p2_keys = {"P2_RIGHT": False,
                         "P2_LEFT": False,
                         "P2_UP": False,
                         "P2_DOWN": False,
                         "P2_LIGHT_PUNCH": False,
                         "P2_MID_PUNCH": False,
                         "P2_HEAVY_PUNCH": False,
                         "P2_LIGHT_KICK": False,
                         "P2_MID_KICK": False,
                         "P2_HEAVY_KICK": False,
                         "P1_ENTER": False,
                         }

        def __str__(self):
            return repr(self)

        # Checks an individual button to see if it is being pressed. Returns boolean value
        def get_down(self, button, controller):
            if self.bmap.game_pad_present:

                return self.bmap.get_down_gamepad(self.bmap.joystick_map[button], controller)
            else:
                return self.bmap.get_down_keyboard(self.bmap.keyboard_map[button])

        # Check each button to see if it is being pressed. Sets button map values to true for buttons pushed
        def handle_input(self):

            for button in self.p1_keys:
                self.p1_keys[button] = self.get_down(button, 0)
            for button in self.p2_keys:
                self.p2_keys[button] = self.get_down(button, 1)

        # Returns just the keys that are active as a list.
        def get_active_keys(self):
            temp = []
            for button in self.p1_keys.keys():
                if self.p1_keys[button]:
                    temp.append(button)
            for button in self.p2_keys.keys():
                if self.p2_keys[button]:
                    temp.append(button)
            return temp

    iHandler = None

    def __init__(self):
        # Singleton to return input handler so every module has the same instance"""
        if not Handler.iHandler:
            Handler.iHandler = Handler.__Handler()

    def __str__(self):
        return str(Handler.iHandler)

    def __getattr__(self, item):
        return getattr(Handler.iHandler, item)