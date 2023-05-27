import math
import pyglet

new_window = pyglet.window.Window()

# Define the number of players and empty lists for positions and sprites
player_Count = 8
position_list = []
sprites = []

# Load the background image
pokerDogs = pyglet.image.load('pokertable.png')
pokerDogs_photo = pyglet.sprite.Sprite(pokerDogs)

# Load the player icon image
pokerPlayerIcon = pyglet.image.load('playerIcon.png')

# Get the window size and the size of the background image
WINDOW_SIZE_X, WINDOW_SIZE_Y = new_window.get_size()[0], new_window.get_size()[1]
pokerDogs_photo_size_x, pokerDogs_photo_size_y = pokerDogs.width, pokerDogs.height

# Calculate the desired size of the player icon based on the window size and player count
PLAYER_ICON_SIZE_X = WINDOW_SIZE_X / (2 * player_Count)
PLAYER_ICON_SIZE_Y = WINDOW_SIZE_Y / (2 * player_Count)

# Scale the background image to fit the window size
pokerDogs_photo.update(scale_x=WINDOW_SIZE_X / pokerDogs_photo_size_x, scale_y=WINDOW_SIZE_Y / pokerDogs_photo_size_y)

# Organize player seat positions geometrically
def seating_position_Generator(total_players):
    ellipse_center = (WINDOW_SIZE_X / 2, WINDOW_SIZE_Y / 2)
    ellipse_radius_x, ellipse_radius_y = WINDOW_SIZE_X / 3, WINDOW_SIZE_Y / 3
    num_divisions = total_players

    for i in range(num_divisions):
        angle = (2 * math.pi * i) / num_divisions
        x = ellipse_center[0] + math.cos(angle) * ellipse_radius_x - PLAYER_ICON_SIZE_X / 2
        y = ellipse_center[1] + math.sin(angle) * ellipse_radius_y - PLAYER_ICON_SIZE_Y / 2
        position_list.append((x, y))
    return position_list

# Generate the seating positions and create sprites for each position
seating_position_Generator(player_Count)

for position in position_list:
    sprite = pyglet.sprite.Sprite(pokerPlayerIcon, x=position[0], y=position[1])
    sprite.scale = PLAYER_ICON_SIZE_X / pokerPlayerIcon.width
    sprites.append(sprite)

print(position_list)

@new_window.event
def on_draw():
    new_window.clear()
    pokerDogs_photo.draw()
    for sprite in sprites:
        sprite.draw()

pyglet.app.run()
