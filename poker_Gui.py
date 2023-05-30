import math
import pyglet
from pyglet.window import mouse
from playerHand import *

new_window = pyglet.window.Window()

# Define the number of players and empty lists for positions and sprites
player_Count = 4
SMALL_BLIND = 5
BIG_BLIND = 10

position_list = []
sprites = []

# Load the background image
pokerTable = pyglet.image.load('pokertable.png')
pokerTable_Sprite = pyglet.sprite.Sprite(pokerTable)

# Load the player icon image
pokerPlayerIcon = pyglet.image.load('playerIcon.png')

#load the dealer button icon image
dealerButton = pyglet.image.load('dealerButton.png')
dealerButton_Sprite = pyglet.sprite.Sprite(dealerButton)

class PlayerSprite(pyglet.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.name = pokerPlayer(str(position_list[random.randint(0,len(position_list))-1]))
        self.current_position = ''

        self.stack_label = pyglet.text.Label(
            f"${self.name.stackSize}",
            font_name='Arial',
            font_size=12,
            x=self.x,
            y=self.y - 20,
            anchor_x='center',
            anchor_y='center'
        )
        self.stack_label_BB = pyglet.text.Label(
            f"{self.name.stackSize/BIG_BLIND} BBs",
            font_name='Arial',
            font_size=12,
            x=self.stack_label.x,
            y=self.stack_label.y - 20,
            anchor_x='center',
            anchor_y='center'
        )
        self.test_Label = pyglet.text.Label(
            f"VPIP: {round(self.name.frequencies.get_VPIP()/100, 2)}",
            font_name='Arial',
            font_size=12,
            x=self.stack_label.x,
            y=self.stack_label_BB.y - 20,
            anchor_x='center',
            anchor_y='center'
        )


    def draw(self):
        super().draw()
        self.stack_label.draw()
        self.stack_label_BB.draw()
        self.test_Label.draw()

    def on_button_click(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print("Button clicked for player with stack size:", self.name.stackSize)


# Get the window size and the size of the background image
WINDOW_SIZE_X, WINDOW_SIZE_Y = new_window.get_size()[0], new_window.get_size()[1]

# Calculate the desired size of the player icon based on the window size and player count
PLAYER_ICON_SIZE_X = WINDOW_SIZE_X / (3 * player_Count)
PLAYER_ICON_SIZE_Y = WINDOW_SIZE_Y / (3 * player_Count)

# Scale the background image to fit the window size
pokerTable_Sprite.update(scale_x=WINDOW_SIZE_X / pokerTable.width, scale_y=WINDOW_SIZE_Y / pokerTable.height)

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
print(current_Hand.dealPreFlop())
print(current_Hand)
#preflop = current_Hand.dealPreFlop()
#flop = current_Hand.dealBoard()
#print(flop)

for i, position in enumerate(position_list):
    stack_size = 1000  # Set the stack size for the player
    sprite = PlayerSprite(image=pokerPlayerIcon, x=position[0], y=position[1])
    sprite.scale = PLAYER_ICON_SIZE_X / pokerPlayerIcon.width
    sprites.append(sprite)

@new_window.event
def on_draw():
    new_window.clear()
    pokerTable_Sprite.draw()

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
