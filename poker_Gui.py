import math
import pyglet
from playerHand import *

new_window = pyglet.window.Window()

# Get the window size and the size of the background image
WINDOW_SIZE_X, WINDOW_SIZE_Y = new_window.get_size()[0], new_window.get_size()[1]

# Define the number of players and empty lists for positions and sprites
player_Count = 6
SMALL_BLIND = 5
BIG_BLIND = 10

position_list = []
button_position_list = []
sprites = []

# Calculate the desired size of the player icon based on the window size and player count
PLAYER_ICON_SIZE_X = WINDOW_SIZE_X / (3 * player_Count)
PLAYER_ICON_SIZE_Y = WINDOW_SIZE_Y / (3 * player_Count)

# Load the background image and scale it to fit the window size
pokerTable = pyglet.image.load('pokertable.png')
pokerTable_Sprite = pyglet.sprite.Sprite(pokerTable)
pokerTable_Sprite.update(scale_x=WINDOW_SIZE_X / pokerTable.width, scale_y=WINDOW_SIZE_Y / pokerTable.height)

# Load the player icon image
pokerPlayerIcon = pyglet.image.load('playerIcon.png')
pokerPlayerIcon_Sprite = pyglet.sprite.Sprite(pokerPlayerIcon)

# Load the dealer button icon image
dealerButton = pyglet.image.load('dealerButton.png')
dealerButton_Sprite = pyglet.sprite.Sprite(dealerButton)
dealerButton_Sprite.update(scale_x=PLAYER_ICON_SIZE_X / dealerButton.width, scale_y=PLAYER_ICON_SIZE_Y / dealerButton.height)


class PlayerSprite(pyglet.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.name = pokerPlayer(str(position_list[random.randint(0, len(position_list) - 1)]), random.randrange(800, 2500, 10))
        self.current_position = ''
        self.scale = PLAYER_ICON_SIZE_X / pokerPlayerIcon.width  # Scale the sprite

        self.stack_label = pyglet.text.Label(
            f"${self.name.getStackSize()}",
            font_name='Arial',
            font_size=12,
            x=self.x,
            y=self.y - 20,
            anchor_x='center',
            anchor_y='center'
        )
        self.stack_label_BB = pyglet.text.Label(
            f"{self.name.getStackSize() / BIG_BLIND} BBs",
            font_name='Arial',
            font_size=12,
            x=self.stack_label.x,
            y=self.stack_label.y - 20,
            anchor_x='center',
            anchor_y='center'
        )
        self.test_Label = pyglet.text.Label(
            f"VPIP: {round(self.name.frequencies.get_VPIP() / 100, 2)}",
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


class CommunityCards():
    def __init__(self, availableCards):
        self.availableCards = availableCards

        # Load card images and determine their sizes
        flop_card1_image = pyglet.image.load('Ad.png')
        flop_card2_image = pyglet.image.load('Ac.png')
        flop_card3_image = pyglet.image.load('Kh.png')
        turn_card_image = pyglet.image.load('playerIcon.png')
        river_card_image = pyglet.image.load('playerIcon.png')
                                                    # Calculate the desired size of the player icon based on the window size and player count
        PLAYER_ICON_SIZE_X = WINDOW_SIZE_X / 3
        PLAYER_ICON_SIZE_Y = WINDOW_SIZE_Y / 3

        self.card_width = flop_card1_image.width / PLAYER_ICON_SIZE_X  # Assuming all cards have the same width
        self.card_height = flop_card1_image.height / PLAYER_ICON_SIZE_Y  # Assuming all cards have the same height

        # Create batches for efficient rendering
        self.flop_batch = pyglet.graphics.Batch()
        self.turn_batch = pyglet.graphics.Batch()
        self.river_batch = pyglet.graphics.Batch()

        # Create sprites for the community cards
        self.flop_card1 = pyglet.sprite.Sprite(flop_card1_image, batch=self.flop_batch)
        self.flop_card2 = pyglet.sprite.Sprite(flop_card2_image, batch=self.flop_batch)
        self.flop_card3 = pyglet.sprite.Sprite(flop_card3_image, batch=self.flop_batch)
        self.turn_card = pyglet.sprite.Sprite(turn_card_image, batch=self.turn_batch)
        self.river_card = pyglet.sprite.Sprite(river_card_image, batch=self.river_batch)

    def calculate_positions(self, window_width, window_height):
        # Calculate the position of the center of the window
        center_x = window_width // 2
        center_y = window_height // 2

        # Position the flop cards
        flop_card1_x = center_x - (1.5 * self.card_width)
        flop_card1_y = center_y - (self.card_height // 2)
        self.flop_card1.position = (flop_card1_x, flop_card1_y)

        flop_card2_x = center_x - (0.5 * self.card_width)
        flop_card2_y = center_y - (self.card_height // 2)
        self.flop_card2.position = (flop_card2_x, flop_card2_y)

        flop_card3_x = center_x + (0.5 * self.card_width)
        flop_card3_y = center_y - (self.card_height // 2)
        self.flop_card3.position = (flop_card3_x, flop_card3_y)

        # Position the turn card
        turn_card_x = center_x - (self.card_width // 2)
        turn_card_y = center_y - (self.card_height // 2) - 20
        self.turn_card.position = (turn_card_x, turn_card_y)

        # Position the river card
        river_card_x = center_x - (self.card_width // 2)
        river_card_y = center_y - (self.card_height // 2) - 40
        self.river_card.position = (river_card_x, river_card_y)

    def set_window_size(self, window_width, window_height):
        self.calculate_positions(window_width, window_height)

    def get_batches(self):
        return self.flop_batch, self.turn_batch, self.river_batch

    def get_cards(self):
        return [self.flop_card1, self.flop_card2, self.flop_card3, self.turn_card, self.river_card]

# Organize player seat positions geometrically
def seating_position_Generator(total_players):
    ellipse_center = (WINDOW_SIZE_X / 2, WINDOW_SIZE_Y / 2)
    ellipse_radius_x, ellipse_radius_y = WINDOW_SIZE_X / 3, WINDOW_SIZE_Y / 3
    num_divisions = total_players

    for i in range(total_players):
        angle = 2 * math.pi * i / num_divisions
        x = ellipse_center[0] + math.cos(angle) * ellipse_radius_x - (PLAYER_ICON_SIZE_X / 2)
        button_X = x - PLAYER_ICON_SIZE_X
        y = ellipse_center[1] + math.sin(angle) * ellipse_radius_y - (PLAYER_ICON_SIZE_Y / 2)
        button_Y = y +  PLAYER_ICON_SIZE_Y
        position_list.append((x, y))
        button_position_list.append((button_X, button_Y))
    return position_list

def buttonPosition():
    
    for i, j in button_position_list:
        dealerButton_Sprite.update(x = i , y = j , scale_x=PLAYER_ICON_SIZE_X / dealerButton.width,
                                scale_y=PLAYER_ICON_SIZE_Y / dealerButton.height)

seating_position_Generator(player_Count)
# Generate the seating positions and create sprites for each position
for i, position in enumerate(position_list):
    stack_size = 1000  # Set the stack size for the player
    sprite = PlayerSprite(image=pokerPlayerIcon, x=position[0], y=position[1])
    sprite.scale = PLAYER_ICON_SIZE_X / pokerPlayerIcon.width
    sprites.append(sprite)

print(button_position_list)
current_Hand = HandGenerator(player_Count)
preflop = current_Hand.dealPreFlop()
flop = current_Hand.dealFlop()
community_cards = CommunityCards(current_Hand.getRemainingCards())

for card in flop:
    community_cards.flop_card1 
# Function to update
def update_window_size(width, height):
    global WINDOW_SIZE_X, WINDOW_SIZE_Y
    
    def update_window_size(width, height):
        global WINDOW_SIZE_X, WINDOW_SIZE_Y
        WINDOW_SIZE_X, WINDOW_SIZE_Y = width, height
        new_window.set_size(WINDOW_SIZE_X, WINDOW_SIZE_Y)
        pokerTable_Sprite.update(scale_x=WINDOW_SIZE_X / pokerTable.width, scale_y=WINDOW_SIZE_Y / pokerTable.height)
        community_cards.set_window_size(WINDOW_SIZE_X, WINDOW_SIZE_Y)

# Event handler for window resize
@new_window.event
def on_resize(width, height):
    update_window_size(width, height)


@new_window.event
def on_draw():
    new_window.clear()
    pokerTable_Sprite.draw()
    dealerButton_Sprite.draw()
    for i,j in button_position_list:
        dealerButton_Sprite
    for sprite in sprites:
        sprite.draw()
    community_cards.get_cards()[0].draw()
    # flop_batch, turn_batch, river_batch = community_cards.get_batches()
    # flop_batch.draw()
    # turn_batch.draw()
    # river_batch.draw()

# Event handler for mouse press
@new_window.event
def on_mouse_press(x, y, button, modifiers):
    for sprite in sprites:
        if sprite.x < x < sprite.x + sprite.width and sprite.y < y < sprite.y + sprite.height:
            sprite.on_button_click(x, y, button, modifiers)

# Start the game
pyglet.app.run()


