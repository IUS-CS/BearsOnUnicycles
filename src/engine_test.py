# This file is just a playground to test the engine with
import engine

s = engine.scene.Scene("Title", "None", set_active=True)
g = engine.game_object.GameObject("Name", set_active=True)
s.add_game_object(g)
g2 = engine.game_object.GameObject("Name2", set_active=True)
g.add_child(g2)
print(s)
print(g)
print(g2)

s.update()
