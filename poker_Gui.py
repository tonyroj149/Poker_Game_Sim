import math
import pyglet
from pyglet.window import mouse
from playerHand import *

new_window = pyglet.window.Window()

# Define the number of players and empty lists for positions and sprites
player_Count = 4
position_list = []
sprites = []

# Load the background image
pokerDogs = pyglet.image.load('pokertable.png')
pokerDogs_photo = pyglet.sprite.Sprite(pokerDogs)

# Load the player icon image
pokerPlayerIcon = pyglet.image.load('playerIcon.png')

class PlayerSprite(pyglet.sprite.Sprite):
    def __init__(self, image, x, y, stack_size):
        super().__init__(image, x, y)
        self.stack_size = stack_size

        self.stack_label = pyglet.text.Label(
            f"{self.stack_size}",
            font_name='Arial',
            font_size=12,
            x=self.x,
            y=self.y - 20,
            anchor_x='center',
            anchor_y='center'
        )
        self.stack_label_BB = pyglet.text.Label(
            f"{self.stack_size} BBs",
            font_name='Arial',
            font_size=12,
            x=self.stack_label.x,
            y=self.stack_label.y - 20,
            anchor_x='center',
            anchor_y='center'
        )

    def draw(self):
        super().draw()
        self.stack_label.draw()

    def on_button_click(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print("Button clicked for player with stack size:", self.stack_size)


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
current_Hand = HandGenerator(player_Count)

for i, position in enumerate(position_list):
    stack_size = 1000  # Set the stack size for the player
    sprite = PlayerSprite(image=pokerPlayerIcon, x=position[0], y=position[1], stack_size=stack_size)
    sprite.scale = PLAYER_ICON_SIZE_X / pokerPlayerIcon.width
    sprites.append(sprite)

@new_window.event
def on_draw():
    new_window.clear()
    pokerDogs_photo.draw()

    # Draw each sprite, including player icons and stack size labels
    for sprite in sprites:
        sprite.draw()

@new_window.event
def on_mouse_press(x, y, button, modifiers):
    # Handle mouse press event
    for sprite in sprites:
        # Check if the mouse press occurred within the bounds of a sprite's button (if it had one)
        if sprite.button.x < x < sprite.button.x + sprite.button.width and sprite.button.y < y < sprite.button.y + sprite.button.height:
            # Perform the desired action for the sprite (e.g., calling on_button_click method)
            sprite.on_button_click(x, y, button, modifiers)


if __name__ == '__main__':
    pyglet.app.run()
