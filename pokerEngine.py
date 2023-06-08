from playerHand import *
from handEvaluator import HandEvaluator
from poker_Gui import *

def start_hand(players, small_blind, big_blind):
    currentHand = CommunityCards()
    currentHand.calculate_positions(WINDOW_SIZE_X, WINDOW_SIZE_Y)
    currentHand_Betting = BettingRound(player_Count, SMALL_BLIND, BIG_BLIND)
    return currentHand

def play_betting_round(betting_round, community_cards=None):
    betting_round.start_next_round()
    if community_cards:
        betting_round.set_community_cards(community_cards)

    while not betting_round.is_betting_round_complete():
        current_player = betting_round.get_current_player()
        # Handle the betting action for the current player
        action = current_player.take_action(betting_round.get_current_bet())
        betting_round.process_action(current_player, action)
        betting_round.update_current_player()

def evaluate_and_award_pot(players, betting_round):
    # Evaluate hands and determine the winner(s)
    print("Evaluating hands...")
    community_cards = betting_round.get_community_cards()
    winners = HandEvaluator.find_winners(players, community_cards)
    print("Winner(s):")
    for winner in winners:
        print(winner)

    # Award the pot to the winner(s) and update chip stacks
    pot = betting_round.get_pot()
    for winner in winners:
        winner.add_chips(pot / len(winners))

def play_game(player_count, small_blind, big_blind):
    # Generate the players
    players = []
    for _ in range(player_count):
        player = Player()
        players.append(player)

    # Create the betting round
    betting_round = BettingRound(players, small_blind, big_blind)

    # Start the hand
    while True:
        deck = start_hand(players, small_blind, big_blind)

        # Preflop round
        print("=== Preflop ===")
        while not betting_round.is_betting_round_complete():
            play_betting_round(betting_round)

        # Flop round
        print("=== Flop ===")
        flop = [deck.draw_card(), deck.draw_card(), deck.draw_card()]
        play_betting_round(betting_round, flop)

        # Turn round
        print("=== Turn ===")
        turn = deck.draw_card()
        play_betting_round(betting_round, [turn])

        # River round
        print("=== River ===")
        river = deck.draw_card()
        play_betting_round(betting_round, [river])

        evaluate_and_award_pot(players, betting_round)

        # Check if any players have run out of chips
        if any(player.get_chip_count() == 0 for player in players):
            print("A player has run out of chips. Game over.")
            break

        # Check if the players want to continue playing another hand
        play_again = input("Do you want to play another hand? (yes/no): ")
        if play_again.lower() != "yes":
            break

    print("Game over.")

# Usage example
play_game(6, 5, 10)

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
