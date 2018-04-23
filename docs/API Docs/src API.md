##Submodules##
===============================


##input_handler module##

###input_handler.ButtonMap###
Holds the button mapping to pygame events regardless of whether via keyboard or game pad

    get_down_gamepad(key, controller)

    get_down_keyboard(key)
       - Using the pygame function to get input.
       - All keys are returned by get_pressed. 
       - We only want the ones we have mapped above so we feed in the index in question to get back what we want

    get_hat_direction(button)

    input = set(['P1_RIGHT', 'P1_MID_KICK', 'P1_MID_PUNCH', 'P1_LEFT', 'P1_HEAVY_KICK', 'P1_UP', 'P1_DOWN', 'P1_LIGHT_KICK', 'P1_HEAVY_PUNCH', 'P1_ENTER', 'P1_LIGHT_PUNCH'])

    joystick_hat_conversion_map_0 = {'P1_DOWN': (1, -1), 'P1_LEFT': (0, -1), 'P1_RIGHT': (0, 1), 'P1_UP': (1, 1)}

    joystick_hat_conversion_map_1 = {'P2_DOWN': (1, -1), 'P2_LEFT': (0, -1), 'P2_RIGHT': (0, 1), 'P2_UP': (1, 1)}

    joystick_map = {'P1_DOWN': 'P1_DOWN', 'P1_ENTER': 9, 'P1_HEAVY_KICK': 2, 'P1_HEAVY_PUNCH': 3, 'P1_LEFT': 'P1_LEFT', 'P1_LIGHT_KICK': 6, 'P1_LIGHT_PUNCH': 4, 'P1_MID_KICK': 1, 'P1_MID_PUNCH': 0, 'P1_RIGHT': 'P1_RIGHT', 'P1_UP': 'P1_UP', 'P2_DOWN': 'P2_DOWN', 'P2_ENTER': 9, 'P2_HEAVY_KICK': 2, 'P2_HEAVY_PUNCH': 3, 'P2_LEFT': 'P2_LEFT', 'P2_LIGHT_KICK': 6, 'P2_LIGHT_PUNCH': 4, 'P2_MID_KICK': 1, 'P2_MID_PUNCH': 0, 'P2_RIGHT': 'P2_RIGHT', 'P2_UP': 'P2_UP'}

    keyboard_map = {'P1_DOWN': 115, 'P1_ENTER': 116, 'P1_HEAVY_KICK': 108, 'P1_HEAVY_PUNCH': 111, 'P1_LEFT': 97, 'P1_LIGHT_KICK': 106, 'P1_LIGHT_PUNCH': 117, 'P1_MID_KICK': 107, 'P1_MID_PUNCH': 105, 'P1_RIGHT': 100, 'P1_UP': 119, 'P2_DOWN': 274, 'P2_ENTER': 13, 'P2_HEAVY_KICK': 113, 'P2_HEAVY_PUNCH': 113, 'P2_LEFT': 276, 'P2_LIGHT_KICK': 113, 'P2_LIGHT_PUNCH': 113, 'P2_MID_KICK': 113, 'P2_MID_PUNCH': 113, 'P2_RIGHT': 275, 'P2_UP': 273}

    set_gamepads()

##input_handler.Handler##

    iHandler = None

##scene_manager module##

	scene_manager.SceneManager(screen, path)

    add_scene(scene)
        - adds a scene to the game, if there are no scenes currently this scene will become active

    change_to_active(title)
        - sets the current scene to title and unloads the other current scene

    change_to_active_background(title)
        - performs the change to active function on a background thread (process) so the main thread doesn’t hang

    update_scene()
        - updates the current scene and passes it to the renderer, animator, and physics

