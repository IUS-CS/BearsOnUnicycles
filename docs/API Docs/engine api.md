Engine
---------------


animation_controller module
---


	animation_controller.AnimationPlayer(sc, surface) 
	

**animation_controller.LoadableAnimator(path, anim, title)**

Bases: pygame.sprite.Group

- This file renders the animations for a game object using pygame

		active = False 

		anim = None 

		current_frame = 0 

		frame_count = 1 

		get_current() 

		location = (0, 0) 

		priority = 0 	

		root_path = '' 

		sprites = [] 

		title = '' 

		update() 

**Group.update(args)**: return None

- Calls the update method of every member sprite. All arguments that were passed to this method are passed to the Sprite update function.


engine.animator module
---



**src.engine.animator.Animation(title, start, count, size, ga)** 

- This file controls the animations for the game objects in the system and should only be used for objects that employ dynamic animations. There must be a sprite object attached to the game object in order to animate it Objects that are statically animated should only use the sprite component
active = False 

		cut_size = (128, 128) 

		frame_count = 1 

		game_object = None 

		load_sprites(path, sheet_size, priority) 
		 	- loads all the sprites for a given animation
		 	based on the path of the spite sheet and
		 	attributes of the animation

		path = '' 

		priority = 0 

		sprites = [] 

		start_coords = (0, 0) 

		title = '' 

**animator.Animator**


Bases: src.engine.component.Component

	add_animation(animation) 
		-adds a possible animation to the animator
		animations = {} 

	build_animation(title, start, count, size, path,
	sheet_size, priority) 
		- constructs a new animation by the given
		parameters and loads the animation with its
		sprites
		
	next_sprite() 
		- changes the sprite image attached to the game
		object to the next frame in the cycle
		
	play(isPlaying) 
		- plays or pauses the current animation	 
	set_current(title) 
		- sets the current playing animation
		- 
	update() 

**animator.AnimatorError**


Bases: exceptions.Exception

**engine.collider**

- This defines the collider classes used in the engine
	
	class src.engine.collider.Collider(lowerP, upperP, cfunc)
	
Bases: src.engine.component.Component

	check_collision() 
		- checks to see if colliding with an object, uses decorated function cfunc

	update() 


engine.collision_manager module
---

**engine.collision_manager.CollisionManager(sc)

- This file runs the logic of collisions with collider objects through the pygame engine and updates during the physics cycle

	check_collisions(g) 
		- checks if a game object is colliding with another game object and returns the result of those collisions
		
	load_game_object(g) 
		- adds a game object”s collider to the collision manager
		
	update() 

engine.component module
---

	component.Component(set_active=False) 

	set_active(active) 

	update() 
		- Perform any logic for one frame
		- 
**engine.game_object module**
	
	src.engine.game_object.GameObject(name, set_active=False, parent=None) 

	add_child(child) 
		- adds a child to this game object

	add_component(component) 
		- adds a component to the game object

	get_child_by_name(name) 
		- Gets a game objects child by name

	get_children_with_component(cType) 
		- Get all children with a certain component

	get_component(cType) 
		- gets a component by type only, throws an exception if the type doesn’t exist

	has_component(cType) 
		- returns whether a game object has a certain component

	remove_child(child) 
		- removes a child from this game object

	set_active(active) 

	set_parent(parent) 
		- sets the parent of this game object
	
	update() 
		- perform any logic on every child and component for one frame REQUIRES TRANSFORM

**engine.game_object.GameObjectError**

Bases: exceptions.BaseException

##engine.scene module
---

- This is the template file for all loadable scenes in the game and stores all the game_objects it controls**

	
		src.engine.scene.Scene(title, background, set_active=False) 

		add_game_object(game_object) 
			- Adds a game obejct to the scene

		get_object_by_name(name) 
			- gets a game obejct by name in the scene and throws an error if not found

		get_objects_of_type(oType) 
			- gets a list of game_objects a specified type

		remove_game_object_by_name(name) 
			- Removes a game_object from the scene throws an error if not found

		set_active(active) 

		update() 
			- perform any logic for one frame on everything in the scene


engine.sprite_renderer module
---

Bases: pygame.sprite.Sprite

- This class loads the files 
	
		engine.sprite_renderer.Loadable(path, spr, location) 
	
		update() 
			- renders self each frame
	
**engine.sprite_renderer**

	src.engine.sprite_renderer.SpriteRenderer(sc, surface) 

	draw_background() 
		- renders the background
	
	load_background() 
		- loads the background image

	load_sprites() 
		- loads the sprite images into the renderer”s queue

	load_sprites_rec(g) 
		- helps load sprites by recurring through the children

	update() 
		- updates the sprites on the screen

engine.transform module
---

	engine.transform.Transform(x=0, y=0, scale=1) 
	
Bases: src.engine.component.Component

- This inherits from component.Component and represents the x,y position of a game_object

		flip_me() 
			- Callback to the animator to flip

		set_flip(b) 
			- Sets the value of flip and changes the value of last flip

		update() 
			- udate the transform of this game object
