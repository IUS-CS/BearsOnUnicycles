Submodules
-----------------


input_handler module
---

**input_handler.ButtonMap**
- Holds the button mapping to pygame events regardless of whether via keyboard or game pad

    	get_down_gamepad(key, controller)

    	get_down_keyboard(key)
      		- Using the pygame function to get input.
       		- All keys are returned by get_pressed. 
       		- We only want the ones we have mapped above so we feed in the index in question to get back what we want

    	get_hat_direction(button)

    	set_gamepads()

**input_handler.Handler**

    iHandler = None

**scene_manager module**

	scene_manager.SceneManager(screen, path)

	add_scene(scene)
        	- adds a scene to the game, if there are no scenes currently this scene will become active

    	change_to_active(title)
        	- sets the current scene to title and unloads the other current scene

    	change_to_active_background(title)
        	- performs the change to active function on a background thread (process) so the main thread doesn’t hang

    	update_scene()
        	- updates the current scene and passes it to the renderer, animator, and physics

