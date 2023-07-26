import tkinter as tk
from tkinter import Tk, Frame, Button, SE, SW
import numpy as np
from PIL import Image, ImageTk
import random
from collections import Counter
import time

card_images = {
    "2♠": "2s.png",
    "3♠": "3s.png",
    "4♠": "4s.png",
    "5♠": "5s.png",
    "6♠": "6s.png",
    "7♠": "7s.png",
    "8♠": "8s.png",
    "9♠": "9s.png",
    "T♠": "Ts.png",
    "J♠": "Js.png",
    "Q♠": "Qs.png",
    "K♠": "Ks.png",
    "A♠": "As.png",
    "2♡": "2h.png",
    "3♡": "3h.png",
    "4♡": "4h.png",
    "5♡": "5h.png",
    "6♡": "6h.png",
    "7♡": "7h.png",
    "8♡": "8h.png",
    "9♡": "9h.png",
    "T♡": "Th.png",
    "J♡": "Jh.png",
    "Q♡": "Qh.png",
    "K♡": "Kh.png",
    "A♡": "Ah.png",
    "2♢": "2d.png",
    "3♢": "3d.png",
    "4♢": "4d.png",
    "5♢": "5d.png",
    "6♢": "6d.png",
    "7♢": "7d.png",
    "8♢": "8d.png",
    "9♢": "9d.png",
    "T♢": "Td.png",
    "J♢": "Jd.png",
    "Q♢": "Qd.png",
    "K♢": "Kd.png",
    "A♢": "Ad.png",
    "2♣": "2c.png",
    "3♣": "3c.png",
    "4♣": "4c.png",
    "5♣": "5c.png",
    "6♣": "6c.png",
    "7♣": "7c.png",
    "8♣": "8c.png",
    "9♣": "9c.png",
    "T♣": "Tc.png",
    "J♣": "Jc.png",
    "Q♣": "Qc.png",
    "K♣": "Kc.png",
    "A♣": "Ac.png"
}

class PokerEngine:
    def __init__(self, num_players, starting_chips):
        self.num_players = num_players
        self.starting_chips = starting_chips
        self.players = []
        self.community_cards = []
        self.pot = 0
        self.current_player_index = 0
        self.small_blind_index = 0
        self.big_blind_index = 0
        self.community_card_labels = []  # Store the community card labels
        self.button_position = 0
        self.deck = []
        self.burned_cards = []
        self.muck = []
    
    def set_button_player(self, player_index):
        self.button_position = player_index
    
    def get_button_player(self):
        return self.players[self.button_position]


    def create_players(self):
        for i in range(self.num_players):
            x, y = player_coords[i]
            player = {
                "name": f"Player {i+1}",
                "chips": self.starting_chips,
                "hand": [],
                "score": 0,
                "folded": False,
                "bet": random.randint(5, 10),  # Random bet between 5 and 10
                "chip_count_label": tk.Label(window, text='test font', font=("Arial", 10))  # Create a label for chip count
            }
            # Calculate the offset for the chip count label
            offset_x = x + player_radius + 30
            offset_y = y - 10

            # Position the chip count label to the side of the player icon
            player["chip_count_label"].place(x=offset_x, y=offset_y)
            self.players.append(player)

    def get_current_player(self):
        return self.players[self.current_player_index]

    def deal_hole_cards(self):
        self.deck = self.create_deck()
        num_players = len(self.players)
        start_index = (self.small_blind_index + 1) % num_players

        # Deal hole cards starting from the player to the left of the button (small blind)
        for i in range(num_players):
            player_index = (start_index + i) % num_players
            player = self.players[player_index]
            player["hand"] = [self.deck.pop(), self.deck.pop()]
            self.display_player_cards(player)

    def create_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']  # Fixed the rank "10" to "T"
        suits = ['♠', '♡', '♢', '♣']
        self.deck = [rank + suit for rank in ranks for suit in suits]
        random.shuffle(self.deck)
        return self.deck
    
    def burn_cards(self, num_cards=None):
        burn= self.deck.pop(num_cards)
        return burn

    def deal_community_cards(self, num_cards):
        self.burned_cards.append(self.burn_cards(1))
        for _ in range(num_cards):
            card = self.deck.pop()
            self.community_cards.append(card)
        self.display_community_cards()

    def display_community_cards(self):
        # Clear previous community card labels
        for label in self.community_card_labels:
            label.destroy()
        self.community_card_labels.clear()

        # Display new community card labels
        for i, card in enumerate(self.community_cards):
            x = start_x + i * (max_card_width + card_frame_padding)
            card_frame = tk.Frame(window, width=max_card_width, height=max_card_height, bg="white", highlightthickness=2, highlightbackground="black")
            card_frame.place(x=x, y=y)
            image_path = card_images[card]
            card_image = Image.open(image_path).resize((max_card_width - 10, max_card_height - 10))
            card_image_tk = ImageTk.PhotoImage(card_image)
            card_label = tk.Label(card_frame, image=card_image_tk)
            card_label.image = card_image_tk
            card_label.pack(fill="both", expand=True)
            self.community_card_labels.append(card_label)

    def display_player_cards(self, player, is_active=True):
        player_index = self.players.index(player)
        x, y = player_coords[player_index]

        num_cards = len(player["hand"])
        card_width = 50  # Width of each card

        total_width = num_cards * card_width  # Calculate the total width of all cards

        start_x = x - (total_width / 2)  # Starting x-coordinate for the first card

        for i in range(num_cards):
            card_x = start_x + (card_width * i)  # Adjust the card position
            card_y = y + 5  # Adjust the card position

            image_path = "facedown.png"  # Path to the face-down card image
            card_image = Image.open(image_path).resize((50, 70))
            card_image_tk = ImageTk.PhotoImage(card_image)

            # Create a label for the card with the facedown image
            card_label = tk.Label(window, image=card_image_tk)
            card_label.image = card_image_tk
            card_label.place(x=card_x, y=card_y)

            if is_active:
                # Reveal the card for active players
                card_label.configure(image=card_image_tk)
                card_label.image = card_image_tk



    def perform_action(self, action):
        player = self.get_current_player()
        if action == "Check":
            print(f"{player['name']} checks.")
        elif action == "Bet":
            print(f"{player['name']} bets.")
        elif action == "Raise":
            print(f"{player['name']} raises.")
        elif action == "Call":
            print(f"{player['name']} calls.")
        elif action == "Fold":
            print(f"{player['name']} folds.")
            player["folded"] = True
        else:
            print("Invalid action.")
            return

        self.next_player()
        self.display_player_cards(player)

    def reset_game(self):
            self.community_cards = []
            for player in self.players:
                player["hand"] = []
                player["score"] = 0
                player["folded"] = False
                player["bet"] = 0
                player["chips"] = self.starting_chips
            self.pot = 0
            self.current_player_index = 0
            self.small_blind_index = 0
            self.big_blind_index = 0


    def get_active_players(self):
        active_players = [player for player in self.players if player["chips"] > 0 and not player["folded"]]
        return active_players
    
    def evaluate_hand(self, hand):
        # Add your implementation of hand evaluation here
        return 0  # Placeholder score for now

    def evaluate_winner(self):
        max_score = max(player["score"] for player in self.players)
        winners = [player for player in self.players if player["score"] == max_score]
        return winners

    def get_tied_players(self):
        max_score = max(player["score"] for player in self.players)
        tied_players = [player for player in self.players if player["score"] == max_score]
        return tied_players

    def take_bets(self):
        active_players = self.get_active_players()
        num_players = len(active_players)
        first_to_act_index = 0
        pot = self.pot

        if num_players == 0:
            print("No active players remaining.")
            return

        if len(active_players) > 1:
            button_index = self.players.index(self.get_button_player())  # Assuming you have a method to get the button player
            first_to_act_index = (button_index + 1) % num_players

        current_player_index = first_to_act_index

        print(f'Press an an action button')

        # Take bets from active players
        for _ in range(num_players):
            player = active_players[current_player_index]

            bet = random.randint(5, 10)  # Retrieve the bet amount
            if bet > player["chips"]:
                print("Invalid bet amount. You don't have enough chips.")
                return

            player["chips"] -= bet
            player["bet"] = bet  # Store the bet amount in the player dictionary
            pot += bet
            current_player_index = (current_player_index + 1) % num_players

        self.pot = pot
        print(f"Total pot: {pot}")

    def distribute_pot(self):
        winners = self.evaluate_winner()
        pot = self.pot
        pot_per_winner = pot // len(winners)
        for winner in winners:
            winner["chips"] += pot_per_winner

    def split_pot(self):
        tied_players = self.evaluate_winner()
        num_players = len(tied_players)
        pot = self.pot
        pot_per_player = pot // num_players
        for player in tied_players:
            player["chips"] += pot_per_player

    def deal_flop(self):
        self.deal_community_cards(3)
        self.take_bets()
        print(f"The flop is {self.community_cards}")
    
    def deal_turn(self):
        self.deal_community_cards(1)
        self.take_bets()
        print(f"The turn is {self.community_cards[3]}")

    def deal_river(self):
        self.deal_community_cards(1)
        self.take_bets()
        print(f"The river is {self.community_cards[4]}")
    
    def play_round(self):
        self.create_deck()
        self.deal_hole_cards()
            
        active_players = self.get_active_players()
        if not active_players:
            print("No active players remaining.")
            return
        
        self.take_bets()
        self.deal_flop()
        time.sleep(4)
        self.deal_turn()
        time.sleep(4)
        self.deal_river()
        print(f'The board is {self.community_cards}')
        print(f'The burned cards: {self.burned_cards}')
        
        # if len(self.community_cards) < 5:
        #     self.deal_community_cards(3)
        #     self.take_bets()
        
        # if len(self.community_cards) < 5:
        #     self.deal_community_cards(1)
        #     self.take_bets()
        
        # if len(self.community_cards) < 5:
        #     self.deal_community_cards(1)
        #     self.take_bets()
        
        for player in self.players:
            hand = player["hand"] + self.community_cards
            player["score"] = self.evaluate_hand(hand)
            print(player["score"])

        winners = self.evaluate_winner()
        
        if winners:
            pot = sum(player["chips"] for player in self.players)
            pot_per_winner = pot // len(winners)
            for winner in winners:
                winner["chips"] += pot_per_winner
            print("Winner(s):")
            for winner in winners:
                print(winner["name"])
            
            # Reveal cards for remaining active players
            for player in active_players:
                self.display_player_cards(player, is_active=True)
        else:
            tied_players = self.get_tied_players()
            pot = sum(player["chips"] for player in tied_players)
            pot_per_player = pot // len(tied_players)
            for player in tied_players:
                player["chips"] += pot_per_player
            print("Tied Players:")
            for player in tied_players:
                print(player["name"])
        
        self.reset_game()
        update_chip_counts()  # Call the method to update the chip counts on the GUI

    
    def initialize_game(self):
        self.create_players()

# Create the main window
window_bg_color = "grey"
window = tk.Tk()
window.title("Texas Hold'em Poker")
window.configure(bg=window_bg_color)

# Set the window size and position
window.geometry("900x700")
window.resizable(False, False)

# Create the table canvas
table_canvas = tk.Canvas(window, width=800, height=600, bg=window_bg_color)
table_canvas.pack(pady=20)

# Draw the elliptical table
table_width = 700
table_height = 500
table_x = (800 - table_width) // 2
table_y = (600 - table_height) // 2
table_canvas.create_oval(table_x, table_y, table_x + table_width, table_y + table_height, outline="brown", width=2)

# Define player positions on the elliptical table
num_players = 4
center_x = table_x + table_width / 2
center_y = table_y + table_height / 2
radius_x = table_width / 2
radius_y = table_height / 2

# Calculate equidistant angles for player positions
angle_step = 2 * np.pi / num_players
player_angles = [i * angle_step for i in range(num_players)]

# Calculate player coordinates on the elliptical table
player_coords = [(center_x + radius_x * np.cos(angle),
                  center_y + radius_y * np.sin(angle)) for angle in player_angles]

# Create frames for community cards
num_community_cards = 5
card_frame_width = 80
card_frame_height = 120
card_frame_padding = 10

# Calculate the available width for the frames
available_width = table_width - (num_community_cards * card_frame_padding)

# Calculate the maximum width and height to fit within the available space
max_card_width = min(card_frame_width, available_width // num_community_cards)
max_card_height = min(card_frame_height, table_height)

# Calculate the starting x-coordinate for the frames with the offset
start_x = table_x + (table_width - (max_card_width * num_community_cards + (num_community_cards - 1) * card_frame_padding)) / 2

# Calculate the y-coordinate for the frames
y = table_y + (table_height - max_card_height) / 2

for i in range(num_community_cards):
    x = start_x + i * (max_card_width + card_frame_padding)
    card_frame = tk.Frame(window, width=max_card_width, height=max_card_height, bg="white", highlightthickness=2, highlightbackground="black")
    card_frame.place(x=x, y=y)

# Load the pot icon image and resize it
pot_icon_path = "pot_icon.png"
pot_icon_size = (30, 30)
pot_icon_image = Image.open(pot_icon_path).resize(pot_icon_size)
pot_icon = ImageTk.PhotoImage(pot_icon_image)

# Calculate the position of the pot icon
pot_icon_x = center_x - pot_icon_size[0] // 2
pot_icon_y = y + max_card_height + 10  # Position below the card frames

# Create the pot icon on the table canvas
table_canvas.create_image(pot_icon_x, pot_icon_y, image=pot_icon)

# Calculate the default player radius based on the table width and number of players
player_radius = min(table_width, table_height) / (2 * num_players)

# Create labels for hand winners and continue playing option
winner_label = tk.Label(window, text="Winner: ", font=("Arial", 12))
winner_label.pack()

continue_var = tk.BooleanVar()
continue_checkbox = tk.Checkbutton(window, text="Continue playing?", variable=continue_var, font=("Arial", 12))
continue_checkbox.pack()

def update_chip_counts():
    for player in engine.players:
        player["chip_count_label"].config(text=f"Chips: {player['chips']}")

def update_community_cards():
    for i, card in enumerate(engine.community_cards):
        x = start_x + i * (max_card_width + card_frame_padding)
        card_frame = tk.Frame(window, width=max_card_width, height=max_card_height, bg="white", highlightthickness=2, highlightbackground="black")
        card_frame.place(x=x, y=y)
        image_path = card_images[card]
        card_image = Image.open(image_path).resize((max_card_width - 10, max_card_height - 10))
        card_image_tk = ImageTk.PhotoImage(card_image)
        card_label = tk.Label(card_frame, image=card_image_tk)
        card_label.image = card_image_tk
        card_label.pack(fill="both", expand=True)

# Create a frame as the container for the poker action buttons
action_button_container = Frame(window)
action_button_container.place(relx=1.0, rely=1.0, anchor=SE)

# Create a frame as the container for the poker action buttons
operating_button_container = Frame(window)
operating_button_container.place(relx=0, rely=1.0, anchor=SW)

# Create the buttons and add them to the container
check_button = Button(action_button_container, text="Check")
bet_button = Button(action_button_container, text="Bet")
raise_button = Button(action_button_container, text="Raise")
call_button = Button(action_button_container, text="Call")
fold_button = Button(action_button_container, text="Fold")
# deal_community_button = tk.Button(operating_button_container, text="Deal Community", command=lambda:engine.deal_community_cards(3))
reset_button= tk.Button(operating_button_container, text="Reset", command=lambda: engine.reset_game())
initialize_button = tk.Button(operating_button_container, text="Start Game", command=lambda:start_game())
# deal_flop_button = tk.Button(operating_button_container, text="Deal Flop", command=lambda:engine.deal_community_cards(3))
# deal_turn_button = tk.Button(operating_button_container, text="Deal Turn", command=lambda:engine.deal_community_cards(1))
# deal_river_button = tk.Button(operating_button_container, text="Deal River", command=lambda:engine.deal_community_cards(1))


check_button.pack(side="left")
bet_button.pack(side="left")
raise_button.pack(side="left")
call_button.pack(side="left")
fold_button.pack(side="left")
# deal_community_button.pack(side="left")
reset_button.pack(side="left")
initialize_button.pack(side="right")
# deal_flop_button.pack(side="left")
# deal_turn_button.pack(side="left")
# deal_river_button.pack(side="left")


# Initialize the PokerEngine
engine = PokerEngine(num_players, starting_chips=1000)

def start_game():
    engine.initialize_game() #create players 
    
    engine.play_round()

# Update the chip count labels
for i, player in enumerate(engine.players):
    player["chip_count_label"].config(text=f"Chips: {player['chips']}")

# Start the GUI event loop
window.mainloop()

