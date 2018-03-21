# This file is just a playground to test the engine with
from src import engine


s = engine.scene.Scene("Title", "None", set_active=True)
g = engine.game_object.GameObject("Name", set_active=True)
s.add_game_object(g)
g2 = engine.game_object.GameObject("Name2", set_active=True)
g.add_child(g2)
g3 = engine.game_object.GameObject("Name3", set_active=True)
g2.add_child(g3)


t = engine.transform.Transform(x=4, y=5)
g.add_component(t)
t2 = engine.transform.Transform(x=6, y=4)
g2.add_component(t2)
t3 = engine.transform.Transform(x=-1, y=7)
g3.add_component(t3)


coll = engine.collision_manager.CollisionManager(s)
rend = engine.sprite_renderer.SpriteRenderer(s)

g.add_component(engine.sprite.Sprite("resources/chun-li.gif", (0, 0), (256, 256)))

g.update()



