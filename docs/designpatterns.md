## Design Patterns Used in SUMOH
	
### Singleton

We have code that handles player input for our game that follows a classical design pattern known as a ***singleton***.  The general purpose[^1\] of a singleton is twofold:  

 -   Make certain that only one instance of a class is created.
-   Provide a global point of access to the object.  

This pattern serves as a good template for our input handler as written below   .

As we only want one class (the __Handler__ class) handling the input for the main game loop, set the dunder method **__init\__**  to ensure any time the Handler class is called, it overrides the default constructor to insures that there is only one unique instance of the class. 

### input_handler.py [^2\]

    import pygame

    class ButtonMap:
        '''Struct that holds the button
        mapping to pygame events'''
    map = {'LEFT': pygame.K_LEFT,
           'RIGHT': pygame.K_RIGHT,
           'UP': pygame.K_UP,
           'DOWN': pygame.K_DOWN,
           'LIGHT_PUNCH': pygame.K_q,
           'MID_PUNCH': pygame.K_w,
           'HEAVY_PUNCH': pygame.K_e,
           'LIGHT_KICK': pygame.K_a,
           'MID_KICK': pygame.K_s,
           'HEAVY_KICK': pygame.K_d,
           'PAUSE': pygame.K_ESCAPE
           }

    def __init__(self):
        pass

    def get_down(self, key):
        '''Use the pygame function to get input'''
        return pygame.key.get_pressed()[self.map[key]]

    def change_mapping(self, key, pygame_constant):
        '''Changes the mapping if it is defined'''
        try:
            self.map[key]  # this will throw KeyError before next line runs
            # key doesn't exist
            self.map[key] = pygame_constant
            return True
        except KeyError:
            return False


    class Handler:
        class __Handler:  # this bit makes it a singleton
            bmap = ButtonMap()
            keys = {}

        def __init__(self):
            self.bMap = ButtonMap()
            # store the value of each predefined input button
            self.keys = {'RIGHT': False,
                         'LEFT': False,
                         'UP': False,
                         'DOWN': False,
                         'LIGHT_PUNCH': False,
                         'MID_PUNCH': False,
                         'HEAVY_PUNCH': False,
                         'LIGHT_KICK': False,
                         'MID_KICK': False,
                         'HEAVY_KICK': False,
                         'PAUSE': False,
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


----------
### Other Patterns
Another patterns we may consider implementing:

 - **Observer pattern**[^3\] -as a means of event handling for the collisions/hit detection for the game combat
 - **Prototype Pattern** -set up a generic "fighter" instance and create new fighters based off the same instance
 
Additional Reading On Gaming Patterns [^4\]


----------
### Current Plan for  Module Development
The three members of our team have had varied experience in developing games using the *Unity* [^5\] game engine. As we share a familiarity with the terminology and organization of this game engine, we have used it as a model for how we develop the game engine using the python package *pygame*. [^6\] Where possible, we are attempted to use object-oriented design in similar ways while instead utilizing the underlying pygame engine.



### Sources and additional Reading
	
[^1\]: [Singleton Description source](http://www.oodesign.com/singleton-pattern.html)
[^2\]:   The most up-to-date version of this code can be found in ***input_handler.py***  Credit to Ben Heil for this code
[^3\]: [Observer Pattern Overview](http://gameprogrammingpatterns.com/observer.html)
[^4\]:[Game Programming Patterns](http://gameprogrammingpatterns.com/contents.html)    
[^5\]:[Unity](https://unity3d.com/unity)
[^6\]:[pygame](https://www.pygame.org/docs/)

