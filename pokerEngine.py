from playerHand import *
from betting import BettingRound

# Define the number of players and blinds
player_count = 6
small_blind = 5
big_blind = 10

# Generate the players
players = []
for _ in range(player_count):
    player = Player()
    players.append(player)

# Create the betting round
betting_round = BettingRound(players, small_blind, big_blind)

# Start the hand
while True:
    print("Starting a new hand...")

    # Reset the players and deck for a new hand
    for player in players:
        player.reset()
    deck = Deck()
    deck.shuffle()

    # Deal the initial hand to each player
    for player in players:
        hand = Hand(deck.draw_card(), deck.draw_card())
        player.receive_hand(hand)

    # Preflop round
    print("=== Preflop ===")
    while not betting_round.is_betting_round_complete():
        current_player = betting_round.get_current_player()
        # Handle the betting action for the current player
        action = current_player.take_action(betting_round.get_current_bet())
        betting_round.process_action(current_player, action)
        betting_round.update_current_player()

    # Flop round
    print("=== Flop ===")
    betting_round.start_next_round()
    # Deal the flop cards
    flop = [deck.draw_card(), deck.draw_card(), deck.draw_card()]
    betting_round.set_community_cards(flop)
    while not betting_round.is_betting_round_complete():
        current_player = betting_round.get_current_player()
        # Handle the betting action for the current player
        action = current_player.take_action(betting_round.get_current_bet())
        betting_round.process_action(current_player, action)
        betting_round.update_current_player()

    # Turn round
    print("=== Turn ===")
    betting_round.start_next_round()
    # Deal the turn card
    turn = deck.draw_card()
    betting_round.set_community_cards([turn])
    while not betting_round.is_betting_round_complete():
        current_player = betting_round.get_current_player()
        # Handle the betting action for the current player
        action = current_player.take_action(betting_round.get_current_bet())
        betting_round.process_action(current_player, action)
        betting_round.update_current_player()

    # River round
    print("=== River ===")
    betting_round.start_next_round()
    # Deal the river card
    river = deck.draw_card()
    betting_round.set_community_cards([river])
    while not betting_round.is_betting_round_complete():
        current_player = betting_round.get_current_player()
        # Handle the betting action for the current player
        action = current_player.take_action(betting_round.get_current_bet())
        betting_round.process_action(current_player, action)
        betting_round.update_current_player()

    # Evaluate hands and determine the winner(s)
    print("Evaluating hands...")
    community_cards = flop + [turn] + [river]
    winners = HandEvaluator.find_winners(players, community_cards)
    print("Winner(s):")
    for winner in winners:
        print(winner)

    # Award the pot to the winner(s) and update chip stacks
    pot = betting_round.get_pot()
    for winner in winners:
        winner.add_chips(pot / len(winners))

    # Check if any players have run out of chips
    if any(player.get_chip_count() == 0 for player in players):
        print("A player has run out of chips. Game over.")
        break

    # Check if the players want to continue playing another hand
    play_again = input("Do you want to play another hand? (yes/no): ")
    if play_again.lower() != "yes":
        break

print("Game over.")



class BettingRound:
    def __init__(self, players, small_blind, big_blind):
        self.players = players
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.current_player_index = 0
        self.bets = {player: 0 for player in players}
        self.folded_players = set()

    def get_current_player(self):
        return self.players[self.current_player_index]

    def update_current_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def fold(self, player):
        self.folded_players.add(player)

    def call(self, player):
        amount_to_call = self.get_amount_to_call(player)
        self.bets[player] += amount_to_call

    def raise_bet(self, player, amount):
        amount_to_call = self.get_amount_to_call(player)
        total_bet = amount_to_call + amount
        self.bets[player] += total_bet

    def get_amount_to_call(self, player):
        current_bet = max(self.bets.values())
        amount_to_call = current_bet - self.bets[player]
        return amount_to_call

    def is_betting_round_complete(self):
        active_players = set(self.players) - self.folded_players
        return len(active_players) <= 1

    def get_pot_size(self):
        return sum(self.bets.values())

    def get_player_bet(self, player):
        return self.bets[player]
