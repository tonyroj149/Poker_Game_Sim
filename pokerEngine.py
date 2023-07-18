import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
import random
from collections import Counter

card_images = {
    "2♠": "2s.png",
    "3♠": "3s.png",
    "4♠": "4s.png",
    "5♠": "5s.png",
    "6♠": "6s.png",
    "7♠": "7s.png",
    "8♠": "8s.png",
    "9♠": "9s.png",
    "10♠": "Ts.png",
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
    "10♡": "Th.png",
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
    "10♢": "Td.png",
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
    "10♣": "Tc.png",
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

    def create_players(self):
        for i in range(self.num_players):
            player = {
                "name": f"Player {i+1}",
                "chips": self.starting_chips,
                "hand": [],
                "score": 0,
                "folded" : False,
                "chip_entry": tk.Entry(window)  # Create an entry widget
            }
            self.players.append(player)
            chip_count_label = tk.Label(window, text=f"Chips: {player['chips']}", font=("Arial", 10))
            chip_count_label.place(x=player_coords[i][0] + player_radius + 5, y=player_coords[i][1] + 20)
            player["chip_count_label"] = chip_count_label
            self.small_blind_index = 0
            self.big_blind_index = 1

    def get_current_player(self):
        return self.players[self.current_player_index]

    def deal_hole_cards(self):
        deck = self.create_deck()
        num_players = len(self.players)
        start_index = self.small_blind_index

        # Deal hole cards starting from the player after the big blind position
        for i in range(num_players):
            player_index = (start_index + i) % num_players
            player = self.players[player_index]
            player["hand"] = [deck.pop(), deck.pop()]
            self.display_player_cards(player)

    def display_player_cards(self, player):
        x, y = player_coords[self.players.index(player)]
        for i in range(len(player["hand"])):
            image_path = "facedown.png"  # Path to the face-down card image
            card_image = Image.open(image_path).resize((50, 70))
            card_image_tk = ImageTk.PhotoImage(card_image)
            card_label = tk.Label(window, image=card_image_tk)
            card_label.image = card_image_tk
            card_label.place(x=x - 50 + (i * 30), y=y + player_radius + 5)

    def create_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['♠', '♡', '♢', '♣']
        deck = [rank + suit for rank in ranks for suit in suits]
        random.shuffle(deck)
        return deck

    def deal_community_cards(self, num_cards):
        deck = self.create_deck()
        for _ in range(num_cards):
            card = deck.pop()
            self.community_cards.append(card)
            self.display_community_cards()

    def display_community_cards(self):
        for i, card in enumerate(self.community_cards):
            x = start_x + i * (max_card_width + card_frame_padding)
            card_frame = tk.Frame(window, width=max_card_width, height=max_card_height, bg="white", highlightthickness=2, highlightbackground="black")
            card_frame.place(x=x, y=y)
            image_path = card_images[card]
            card_image = Image.open(image_path).resize((max_card_width - 10, max_card_height - 10))
            card_image_tk = ImageTk.PhotoImage(card_image)
            card_label = tk.Label(card_frame, image=card_image_tk)
            card_label.image = card_image_tk  # Store a reference to the image to prevent garbage collection
            card_label.pack(fill="both", expand=True)

    def reset_game(self):
        self.community_cards = []
        for player in self.players:
            player["hand"] = []
            player["score"] = 0

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

    def take_bets(self, first_to_act_index=None):
        active_players = self.get_active_players()
        num_players = len(active_players)
        pot = self.pot
        current_player_index = first_to_act_index

        # Take bets from active players
        for _ in range(num_players):
            player = active_players[current_player_index]
            bet = player["chip_entry"].get()
            if not bet.isdigit():
                print("Invalid bet amount. Please enter a numeric value.")
                return
            bet = int(bet)
            if bet > player['chips']:
                print("Invalid bet amount. You don't have enough chips.")
                return
            player['chips'] -= bet
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
    
    def play_round(self):
        self.deal_hole_cards()
        self.take_bets()
        if len(self.community_cards) < 5:
            self.deal_community_cards(3)
            self.take_bets()
        if len(self.community_cards) < 5:
            self.deal_community_cards(1)
            self.take_bets()
        if len(self.community_cards) < 5:
            self.deal_community_cards(1)
            self.take_bets()
        for player in self.players:
            hand = player["hand"] + self.community_cards
            player["score"] = self.evaluate_hand(hand)

        winners = self.evaluate_winner()

        if winners:
            pot = sum(player["chips"] for player in self.players)
            pot_per_winner = pot // len(winners)
            for winner in winners:
                winner["chips"] += pot_per_winner
            print("Winner(s):")
            for winner in winners:
                print(winner["name"])
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

# Create the main window
window = tk.Tk()
window.title("Texas Hold'em Poker")

# Set the window size and position
window.geometry("900x700")
window.resizable(False, False)

# Create the table canvas
table_canvas = tk.Canvas(window, width=800, height=600, bg="green")
table_canvas.pack(pady=20)

# Draw the elliptical table
table_width = 700
table_height = 500
table_x = (800 - table_width) // 2
table_y = (600 - table_height) // 2
table_canvas.create_oval(table_x, table_y, table_x + table_width, table_y + table_height, outline="brown", width=2)

# Define player positions on the elliptical table
num_players = 8
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

# Draw players on the table
player_radius = 20
chip_count_labels = []  # List to store chip count labels
for i, (x, y) in enumerate(player_coords):
    table_canvas.create_oval(x - player_radius, y - player_radius,
                             x + player_radius, y + player_radius, fill="white")
    player_label = tk.Label(window, text=f"Player {i+1}", font=("Arial", 10))
    player_label.place(x=x+player_radius+5, y=y)  # Position label next to player icon
    chip_count_label = tk.Label(window, text="Chips: 0", font=("Arial", 10))
    chip_count_label.place(x=x+player_radius+5, y=y+20)  # Position label below player icon
    chip_count_labels.append(chip_count_label)

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

# Initialize the PokerEngine
engine = PokerEngine(num_players, starting_chips=1000)
engine.create_players()

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

def reset_game():
    engine.reset_game()
    update_community_cards()
    winner_label.config(text="Winner: ")
    continue_var.set(False)

def play_round_button():
    engine.play_round()
    update_chip_counts()

def deal_community_button():
    engine.deal_community_cards(3)
    update_community_cards()
    engine.take_bets()

play_round_button = tk.Button(window, text="Play Round", command=play_round_button)
play_round_button.pack(side=tk.LEFT, padx=10, pady=10)

deal_community_button = tk.Button(window, text="Deal Community", command=deal_community_button)
deal_community_button.pack(side=tk.LEFT, padx=10, pady=10)


# Simulation Loop
num_rounds = 1
engine.play_round()
# Update the chip count labels
for i, player in enumerate(engine.players):
    chip_count_labels[i].config(text=f"Chips: {player['chips']}")

# Start the GUI event loop
window.mainloop()
