import pyglet


pokerDogs = pyglet.image.load('pokertable.png')
pokerDogs_photo = pyglet.sprite.Sprite(pokerDogs)

new_window = pyglet.window.Window()

# label = pyglet.text.Label('Hello, World !',
#                           font_name ='Cooper',
#                           font_size = 16,
#                           x = new_window.width//2, 
#                           y = new_window.height//2,
#                           anchor_x ='center', 
#                           anchor_y ='center')

@new_window.event
def on_draw():
    # new_window.clear()
    #label.draw()
    pokerDogs_photo.draw()

pyglet.app.run()