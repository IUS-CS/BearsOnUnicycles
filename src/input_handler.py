# File: input_handler.py
# Authors: BearsOnUnicycles
# Since: 3/10/18
import pygame


class ButtonMap:
    '''Struct that holds the button
    mapping to pygame events'''

    map = {'RIGHT': pygame.K_RIGHT,   \
            'LEFT': pygame.K_LEFT,    \
            'UP'  : pygame.K_UP,      \
            'DOWN': pygame.K_DOWN,    \
     'LIGHT_PUNCH': pygame.K_q,       \
      'MID_PUNCH' : pygame.K_w,       \
     'HEAVY_PUNCH': pygame.K_e,       \
      'LIGHT_KICK': pygame.K_a,       \
        'MID_KICK': pygame.K_s,       \
      'HEAVY_KICK': pygame.K_d,       \
           'PAUSE':pygame.K_ESCAPE    \
    }


    def __init__(self):
        pass

    def get_down(self, key):
        '''Use the pygame function to get input'''
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
            self.bMap = ButtonMap()
            # store the value of each predefined input button
            self.keys={'RIGHT': False,    \
                        'LEFT': False,    \
                        'UP'  : False,    \
                        'DOWN': False,    \
                 'LIGHT_PUNCH': False,    \
                  'MID_PUNCH' : False,    \
                 'HEAVY_PUNCH': False,    \
                  'LIGHT_KICK': False,    \
                    'MID_KICK': False,    \
                  'HEAVY_KICK': False,    \
                       'PAUSE': False,    \
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

    iHandler = None

    def __init__(self):
        '''Singleton to return
        input handler so every module
        has the same instance'''
        if not Handler.iHandler:
            Handler.iHandler = Handler.__Handler()
            print(True)

    def __str__(self):
        return str(Handler.iHandler)

    def __getattr__(self, item):
        return getattr(Handler.iHandler, item)




