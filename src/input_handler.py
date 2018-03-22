# File: input_handler.py
# Authors: BearsOnUnicycles
# Since: 3/10/18
# this file handles all the input from the keyboard
import pygame


class ButtonMap:
    '''Struct that holds the button
    mapping to pygame events'''
    game_pad_present = False  #determines which button map to use
    game_pads = []
    map = {}

    default = {'P1_RIGHT': pygame.K_RIGHT,   \
            'P1_LEFT': pygame.K_LEFT,    \
            'P1_UP'  : pygame.K_UP,      \
            'P1_DOWN': pygame.K_DOWN,    \
     'P1_LIGHT_PUNCH': pygame.K_q,       \
      'P1_MID_PUNCH' : pygame.K_w,       \
     'P1_HEAVY_PUNCH': pygame.K_e,       \
      'P1_LIGHT_KICK': pygame.K_a,       \
        'P1_MID_KICK': pygame.K_s,       \
      'P1_HEAVY_KICK': pygame.K_d,       \
           'P1_PAUSE':pygame.K_ESCAPE    \
    }





    '''detect how many controllers are connected,
        determine which mapping to use,
        initialize each controller,
        display the name of that controller
    '''
    def set_gamepads(self):
        pygame.joystick.init() #must be done before other joystick functions work
        if pygame.joystick.get_count() > 0:
            self.game_pad_present = True
            count = pygame.joystick.get_count()
            print(count, " game pads detected")
            for i in range((count)):
            # add controller to joystick list
                self.game_pads.append(pygame.joystick.Joystick(i))
                self.game_pads[i].init() #must be initialized in the list
                print('.Game pad detected: {} assigned to player {}'.format(self.game_pads[i].get_name(), (i+1) ))
                i = i+1

                self.map = {'P1_RIGHT': 5, \
                           'P1_LEFT': 7, \
                           'P1_UP': 4, \
                           'P1_DOWN': 6, \
                           'P1_LIGHT_PUNCH': pygame.K_q, \
                           'P1_MID_PUNCH': pygame.K_w, \
                           'P1_HEAVY_PUNCH': pygame.K_e, \
                           'P1_LIGHT_KICK': pygame.K_a, \
                           'P1_MID_KICK': pygame.K_s, \
                           'P1_HEAVY_KICK': pygame.K_d, \
                           'P1_PAUSE': pygame.K_ESCAPE, \

                           'P2_LEFT': pygame.K_LEFT, \
                           'P2_UP': pygame.K_UP, \
                           'P2_DOWN': pygame.K_DOWN, \
                           'P2_LIGHT_PUNCH': pygame.K_q, \
                           'P2_MID_PUNCH': pygame.K_w, \
                           'P2_HEAVY_PUNCH': pygame.K_e, \
                           'P2_LIGHT_KICK': pygame.K_a, \
                           'P2_MID_KICK': pygame.K_s, \
                           'P2_HEAVY_KICK': pygame.K_d, \
                           'P2_PAUSE': pygame.K_ESCAPE \
                           }
        else:
            self.map = self.default

    def __init__(self):
        self.set_gamepads()


    def get_down(self, key):
        '''Use the pygame function to get input'''
        if self.game_pad_present:
            return self.game_pads[0].get_button(7)
        else:
            return pygame.key.get_pressed()[self.map[key]]

    def change_mapping(self, key, pygame_constant):
        '''Changes the mapping if it is defined'''
        try:
            self.map[key] # this will throw KeyError before next line runs
                          # key doesn't exist
            self.map[key] = pygame_constant
            return True
        except KeyError:
            return False


class Handler:
    class __Handler: # this bit makes it a singleton
        bmap = ButtonMap()
        keys = {}
        def __init__(self):

            # store the value of each predefined input button
            self.keys={'P1_RIGHT': False,    \
                        'P1_LEFT': False,    \
                        'P1_UP'  : False,    \
                        'P1_DOWN': False,    \
                 'P1_LIGHT_PUNCH': False,    \
                  'P1_MID_PUNCH' : False,    \
                 'P1_HEAVY_PUNCH': False,    \
                  'P1_LIGHT_KICK': False,    \
                    'P1_MID_KICK': False,    \
                  'P1_HEAVY_KICK': False,    \
                       'P1_PAUSE': False, \
 \
                       'P2_RIGHT': False, \
                       'P2_LEFT': False, \
                       'P2_UP': False, \
                       'P2_DOWN': False, \
                       'P2_LIGHT_PUNCH': False, \
                       'P2_MID_PUNCH': False, \
                       'P2_HEAVY_PUNCH': False, \
                       'P2_LIGHT_KICK': False, \
                       'P2_MID_KICK': False, \
                       'P2_HEAVY_KICK': False, \
                       'P2_PAUSE': False, \
                       }

        def __str__(self):
            return repr(self)

        def handle_input(self):
            '''The big input switch
            statement that quantifies all
            the input'''
            for key in self.bmap.map.keys():
                self.keys[key] = self.bmap.get_down(key)

        def get_down(self, key):
            return self.keys[key]

        def get_active_keys(self):
            temp = []
            for key in self.keys.keys():
                if self.keys[key]:
                    temp.append(key)
            return temp

    iHandler = None

    def __init__(self):
        '''Singleton to return
        input handler so every module
        has the same instance'''
        if not Handler.iHandler:
            Handler.iHandler = Handler.__Handler()

    def __str__(self):
        return str(Handler.iHandler)

    def __getattr__(self, item):
        return getattr(Handler.iHandler, item)




