import random
from poker_utils import evaluate_hand


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
        self.minimum_bet = 0

    def create_players(self):
        for i in range(self.num_players):
            player = {
                "name": f"Player {i+1}",
                "chips": self.starting_chips,
                "hand": [],
                "folded": False
            }
            self.players.append(player)

    def deal_hole_cards(self):
        deck = self.create_deck()
        num_players = len(self.players)
        start_index = self.small_blind_index

        # Deal hole cards starting from the player after the big blind position
        for i in range(num_players):
            player_index = (start_index + i) % num_players
            player = self.players[player_index]
            player["hand"] = [deck.pop(), deck.pop()]

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

    def reset_game(self):
        self.community_cards = []
        for player in self.players:
            player["hand"] = []
            player["folded"] = False

    def get_active_players(self):
        active_players = [player for player in self.players if player["chips"] > 0 and not player["folded"]]
        return active_players

    def get_next_active_player(self):
        num_players = len(self.players)
        for _ in range(num_players):
            self.current_player_index = (self.current_player_index + 1) % num_players
            player = self.players[self.current_player_index]
            if not player["folded"]:
                return player

    def take_blinds(self):
        small_blind_player = self.players[self.small_blind_index]
        big_blind_player = self.players[self.big_blind_index]

        small_blind_amount = min(self.minimum_bet, small_blind_player["chips"])
        big_blind_amount = min(self.minimum_bet * 2, big_blind_player["chips"])

        small_blind_player["chips"] -= small_blind_amount
        big_blind_player["chips"] -= big_blind_amount

        self.pot += small_blind_amount + big_blind_amount

    def take_bets(self, first_to_act_index=None):
        active_players = self.get_active_players()
        num_players = len(active_players)
        current_bet = 0
        current_raise = self.minimum_bet

        while len(set(player["chips"] for player in active_players)) > 1:
            player = self.get_next_active_player()

            print(f"Current player: {player['name']}")

            if current_bet > 0:
                print(f"Current bet: {current_bet}")
            if current_raise > 0:
                print(f"Current raise: {current_raise}")

            action = input("Choose an action (fold/check/bet/raise): ")

            if action == "fold":
                player["folded"] = True
                print(f"{player['name']} folds.")
                continue

            if action == "check":
                if current_bet == 0:
                    print(f"{player['name']} checks.")
                    continue
                else:
                    print(f"{player['name']} cannot check. Please bet or fold.")
                    continue

            if action == "bet":
                bet_amount = int(input("Enter bet amount: "))
                if bet_amount >= player["chips"]:
                    print("Invalid bet amount. You don't have enough chips. Please bet a lower amount.")
                    continue
                if bet_amount < current_bet + self.minimum_bet:
                    print("Invalid bet amount. The bet must be equal to or greater than the current bet + minimum bet.")
                    continue
                player["chips"] -= bet_amount
                self.pot += bet_amount
                current_bet = bet_amount
                current_raise = bet_amount - self.minimum_bet
                print(f"{player['name']} bets {bet_amount}.")
                continue

            if action == "raise":
                raise_amount = int(input("Enter raise amount: "))
                if raise_amount >= player["chips"]:
                    print("Invalid raise amount. You don't have enough chips. Please raise a lower amount.")
                    continue
                if raise_amount < current_raise:
                    print("Invalid raise amount. The raise must be greater than or equal to the current raise.")
                    continue
                player["chips"] -= raise_amount
                self.pot += raise_amount
                current_bet += raise_amount
                current_raise = raise_amount - self.minimum_bet
                print(f"{player['name']} raises to {current_bet}.")
                continue

        print("Betting round complete.")

    def evaluate_hand(self, hand):
        return evaluate_hand(hand)

    def evaluate_winner(self):
        best_hand_score = None
        winners = []

        for player in self.players:
            hand = player["hand"] + self.community_cards
            hand_score = self.evaluate_hand(hand)

            if best_hand_score is None or hand_score > best_hand_score:
                best_hand_score = hand_score
                winners = [player]
            elif hand_score == best_hand_score:
                winners.append(player)

        return winners


    def play_round(self):
        self.deal_hole_cards()
        self.take_bets(first_to_act_index=self.current_player_index)
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



    def play_game(self):
        self.create_players()

        while True:
            self.play_round()
            choice = input("Continue to the next round? (y/n): ")
            if choice.lower() != "y":
                break


# Example usage
engine = PokerEngine(num_players=4, starting_chips=1000)
engine.small_blind_index = 0
engine.big_blind_index = 1
engine.play_game()
