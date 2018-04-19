# File: scene_manager.py
# Authors: BearsOnUnicycles
# Since: 3/25/18
# This file handles the loading and unloading of scenes by connecting the active scene to the various systems of the
#   engine

from src import engine
import threading


class SceneManager:

    surface = None
    active_scene = None
    scenes = {}
    renderer = None
    animator = None
    physics = None
    root_path = ""

    def __init__(self, screen, path):
        self.surface = screen       # pygame surface
        self.active_scene = None    # the current scene
        self.scenes = {}            # key = scene.title, value = scene
        self.renderer = None        # engine.sprite_renderer.SpriteRenderer
        self.animator = None        # engine.animation_controller.AnimationPlayer
        self.physics = None         # engine.collision_manager.CollisionManager
        self.root_path = path       # the path to the dir that contains src

    def add_scene(self, scene):
        '''adds a scene to the game, if there are
        no scenes currently this scene will become
        active'''
        self.scenes[scene.title] = scene
        if self.active_scene is None:
            self.change_to_active(scene.title)

    def change_to_active(self, title):
        '''sets the current scene to title and
        unloads the other current scene'''
        print("Loading Scene {}...".format(title))
        scene = self.scenes[title]
        print("Loading Sprites...")
        renderer = engine.sprite_renderer.SpriteRenderer(scene, self.surface)
        print("Loading Animations...")
        animator = engine.animation_controller.AnimationPlayer(scene, self.surface)
        if self.physics is None:
            print("Initializing Physics...")
            self.physics = engine.collision_manager.CollisionManager(scene)
        else:
            self.physics.sc = scene
        self.renderer = renderer
        self.animator = animator
        self.active_scene = scene
        print("Scene Loaded")

    def change_to_active_background(self, title):
        """performs the change to active function
        on a background thread (process) so the main thread doesn't hang"""
        print("Creating Load Thread for {}...".format(title))
        t = threading.Thread(name="Loading Thread", target=self.change_to_active, args=(title,))
        t.setDaemon(True)
        t.start()

    def update_scene(self):
        '''updates the current scene and passes it
        to the renderer, animator, and physics'''
        if self.active_scene is not None:
            self.physics.update()
            self.active_scene.update()
            self.renderer.draw_background()
            self.animator.update()
            self.renderer.update()


