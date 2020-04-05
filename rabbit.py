import pyglet as pyglet
from game.platform import Platform
from game.small_tree import SmallTree
from game.large_tree import LargeTree
from game.bush import Bush
from game.cloud import Cloud
from game.bridge import Bridge
from game.resources import rabbit_images
from game.rabbit import Rabbit
import pymunk
from pymunk import Vec2d

window_width = 960
window_height = 832

window = pyglet.window.Window(window_width, window_height)
world_batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)



score_label = pyglet.text.Label(text="Score: 0", x=0, y=820, batch=world_batch)


# Physics stuff
space = pymunk.Space()
space.gravity = Vec2d(0.0, -900.0)


#g1 = Platform(window=window, batch=world_batch, group=background)
#g1.create(hpos=6, vpos=2, size=5)

p2 = Platform(window=window, batch=world_batch, group=background, space=space)
p2.create(hpos=0, vpos=15, size=5)
p3 = Platform(window=window, batch=world_batch, group=background, space=space)
p3.create(hpos=16, vpos=15, size=8)
b1 = Bridge(window=window, batch=world_batch, group=background, space=space)
b1.create(hpos=3, vpos=16, size=15)

p4 = Platform(window=window, batch=world_batch, group=background, space=space)
p4.create(hpos=25, vpos=17, size=6)

t1 = LargeTree(window=window, batch=world_batch, group=background)
t1.create(hpos=27, vpos=18)

rabbit = Rabbit(x=100, y=800, batch=world_batch, group=background, space=space)


# t1 = SmallTree(window=window, batch=world_batch, group=background)
# t1.create(hpos=5, vpos=1)
#
# t2 = LargeTree(window=window, batch=world_batch, group=background)
# t2.create(hpos=15, vpos=10)
#
# b1 = Bush(window=window, batch=world_batch, group=background)
# b1.create(hpos=11, vpos=12)
#
# c1 = Cloud(window=window, batch=world_batch, group=background)
# c1.create(hpos=20, vpos=15)


#t1 = SmallTree(window=window, batch=world_batch, group=background)
#t1.create(hpos=7, vpos=6)

#t1 = SmallTree(window=window, batch=world_batch, group=background)
#t1.create(hpos=11, vpos=7)

# g2 = Bridge(window=window, batch=world_batch, group=background)
# g2.create(hpos=0, vpos=2, size=20)

window.push_handlers(rabbit.key_handler)


def init():
    global score

    score = 0
    score_label.text = "Score: " + str(score)


@window.event
def on_draw():
    window.clear()
    world_batch.draw()
    ps = rabbit.shape.get_vertices()
    ps = [p.rotated(rabbit.body.angle) + rabbit.body.position for p in ps]
    n = len(ps)
    ps = [c for p in ps for c in p]
    pyglet.graphics.draw(n, pyglet.gl.GL_LINE_LOOP,
             ('v2f', ps), ('c3f', (1, 0, 0)*n))



def update(dt):
    global score
    dt = 1.0/120.

    space.step(dt)

    rabbit.update(dt)

if __name__ == "__main__":
    # Start it up!
    init()

    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / 120.0)


    # Tell pyglet to do its thing
    pyglet.app.run()