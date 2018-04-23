# File: load_arena.py
# Author: BearsOnUnicycles
# Since: 4/17/18
# This is the loading screen for the arena

from src import engine, scenes


class LoadArena(engine.scene.Scene):
    manager = None
    activated = False  # have we started loading the scene?

    def __init__(self, manager, background, player1_name, player2_name, UI=False):
        super(LoadArena, self).__init__("Load Arena", "/src/resources/levels/GreenBackGround.png", set_active=True)
        self.manager = manager
        self.manager.add_scene(scenes.arena.Arena(manager, background, player1_name, player2_name, UI))
        g = engine.game_object.GameObject("buffer", set_active=True)
        g.add_component(engine.transform.Transform())
        g.add_component(engine.sprite.Sprite("/src/resources/levels/LoadingTutorial.png", (0, 50), (800, 500),
                                             1))  # todo this needs to animate
        self.add_game_object(g)
        self.activated = False

    def update(self):
        super(LoadArena, self).update()
        if not self.activated:
            self.activated = True
            self.manager.change_to_active_background("arena")
