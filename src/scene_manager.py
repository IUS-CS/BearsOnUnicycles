# File: scene_manager.py
# Authors: BearsOnUnicycles
# Since: 3/25/18
# This file handles the loading and unloading of scenes by connecting the active scene to the various systems of the
#   engine

from src import engine


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
        scene = self.scenes[title]
        self.renderer = engine.sprite_renderer.SpriteRenderer(scene, self.surface)
        self.animator = engine.animation_controller.AnimationPlayer(scene, self.surface)
        self.physics = engine.collision_manager.CollisionManager(scene)
        self.active_scene = scene

    def update_scene(self):
        '''updates the current scene and passes it
        to the renderer, animator, and physics'''
        if self.active_scene is not None:
            self.active_scene.update()
            self.renderer.update()
            self.animator.update()
            self.physics.update()
