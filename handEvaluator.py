class HandEvaluator:
    @staticmethod
    def find_winners(players, community_cards):
        winners = []
        best_hand_rank = -1

        for player in players:
            complete_hand = player.get_hand() + community_cards
            hand_rank = HandEvaluator.evaluate_hand(complete_hand)

            if hand_rank > best_hand_rank:
                best_hand_rank = hand_rank
                winners = [player]
            elif hand_rank == best_hand_rank:
                winners.append(player)

        return winners

    @staticmethod
    def evaluate_hand(hand):
        # Implement your hand evaluation logic here
        # Evaluate the strength of the hand and return a hand rank
        # You can assign different ranks to different hand combinations

        # Example implementation (using a simplified hand ranking system)
        hand_rank = 0

        # Check for Royal Flush
        if HandEvaluator.has_royal_flush(hand):
            hand_rank = 9
        # Check for Straight Flush
        elif HandEvaluator.has_straight_flush(hand):
            hand_rank = 8
        # Check for Four of a Kind
        elif HandEvaluator.has_four_of_a_kind(hand):
            hand_rank = 7
        # Check for Full House
        elif HandEvaluator.has_full_house(hand):
            hand_rank = 6
        # Check for Flush
        elif HandEvaluator.has_flush(hand):
            hand_rank = 5
        # Check for Straight
        elif HandEvaluator.has_straight(hand):
            hand_rank = 4
        # Check for Three of a Kind
        elif HandEvaluator.has_three_of_a_kind(hand):
            hand_rank = 3
        # Check for Two Pair
        elif HandEvaluator.has_two_pair(hand):
            hand_rank = 2
        # Check for One Pair
        elif HandEvaluator.has_one_pair(hand):
            hand_rank = 1
        # High Card (default)
        else:
            hand_rank = 0

        return hand_rank

    # Implement additional helper methods for checking different hand combinations

    @staticmethod
    def has_royal_flush(hand):
        # Check if the hand contains a Royal Flush
        # Implement the logic to check for a Royal Flush

    @staticmethod
    def has_straight_flush(hand):
        # Check if the hand contains a Straight Flush
        # Implement the logic to check for a Straight Flush

    @staticmethod
    def has_four_of_a_kind(hand):
        # Check if the hand contains Four of a Kind
        # Implement the logic to check for Four of a Kind

    @staticmethod
    def has_full_house(hand):
        # Check if the hand contains a Full House
        # Implement the logic to check for a Full House

    @staticmethod
    def has_flush(hand):
        # Check if the hand contains a Flush
        # Implement the logic to check for a Flush

    @staticmethod
    def has_straight(hand):
        # Check if the hand contains a Straight
        # Implement the logic to check for a Straight

    @staticmethod
    def has_three_of_a_kind(hand):
        # Check if the hand contains Three of a Kind
        # Implement the logic to check for Three of a Kind

    @staticmethod
    def has_two_pair(hand):
        # Check if the hand contains Two Pair
        # Implement the logic to check for Two Pair

    @staticmethod
    def has_one_pair(hand):
        # Check if the hand contains One Pair
        # Implement the logic to check for One Pair

    @staticmethod
    def has_high_card(hand):
        # Check if the hand contains High Card
        # Implement the logic to check for High Card
