import pyglet

# access the config of the context
window = pyglet.window.Window()
context = window.context
config = context.config

print("config.double_buffer: ", config.double_buffer)
print("config.stereo: ", config.stereo)
print("config.sample_buffers: ", config.sample_buffers)
print("config.major_version: ", config.major_version)

#  Platform which provides access to the display(s)
platform = pyglet.window.get_platform()
print("platform: ", platform)

# a Display is a collection of “screens” 
# attached to a single display device
display = platform.get_default_display()
print("display: ", display)

for screen in display.get_screens():
    print(screen)