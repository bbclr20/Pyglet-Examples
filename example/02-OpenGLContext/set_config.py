import pyglet

# construct a Config and set the attribute
config = pyglet.gl.Config(alpha_size=8)
window = pyglet.window.Window(config=config) # default context


# construct a Context
platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_default_screen()

template = pyglet.gl.Config(sample_buffers=1, samples=4)
try:
    config = screen.get_best_config(template)
except pyglet.window.NoSuchConfigException as err:
    print(err)
    template = gl.Config()
    config = screen.get_best_config(template)

context = config.create_context(None)
window = pyglet.window.Window(context=context)

@window.event
def on_draw():
    window.clear()

pyglet.app.run()