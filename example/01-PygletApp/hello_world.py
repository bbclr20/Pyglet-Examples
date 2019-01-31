import pyglet
from pyglet.window import key, mouse

# set pyglet resource dir
image_path = "../../assets/image"
pyglet.resource.path = [image_path]

# create window, text and image objects
window = pyglet.window.Window()
label = pyglet.text.Label(
                        "Hello world",
                        font_name="Times New Roman",
                        font_size=36,
                        x=window.width//2, 
                        y=window.height//2,
                        anchor_x="center", 
                        anchor_y="center"
                        )
image = pyglet.resource.image("mini.jpg")
                                     
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print("A")

    if symbol == key.LEFT:
        print("LEFT")
    
    if symbol == key.ENTER:
        print("ENTER")

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print("mouse left")

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
    label.draw()

if __name__ == "__main__":
    pyglet.app.run()
