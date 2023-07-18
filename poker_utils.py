from collections import Counter

def evaluate_hand(self, hand):
    hand_ranking = [
        "High Card",
        "One Pair",
        "Two Pairs",
        "Three of a Kind",
        "Straight",
        "Flush",
        "Full House",
        "Four of a Kind",
        "Straight Flush",
        "Royal Flush"
    ]

    ranks = [card[:-1] for card in hand]
    suits = [card[-1] for card in hand]

    counter = Counter(ranks)
    rank_counts = counter.most_common()

    # Check for Royal Flush
    if set(hand) == {"10♠", "J♠", "Q♠", "K♠", "A♠"} or \
            set(hand) == {"10♡", "J♡", "Q♡", "K♡", "A♡"} or \
            set(hand) == {"10♢", "J♢", "Q♢", "K♢", "A♢"} or \
            set(hand) == {"10♣", "J♣", "Q♣", "K♣", "A♣"}:
        return hand_ranking.index("Royal Flush")

    # Check for Straight Flush
    straight_flush_suit = None
    for suit in suits:
        if suits.count(suit) >= 5:
            straight_flush_suit = suit
            break

    if straight_flush_suit:
        straight_flush_ranks = [rank for rank, suit in zip(ranks, suits) if suit == straight_flush_suit]
        straight_flush_ranks.sort(key=lambda x: ranks.index(x) if x != 'A' else -1)

        if len(straight_flush_ranks) >= 5:
            straight_flush = [rank + straight_flush_suit for rank in straight_flush_ranks[-5:]]
            if set(straight_flush) == {"2♠", "3♠", "4♠", "5♠", "6♠"} or \
                    set(straight_flush) == {"2♡", "3♡", "4♡", "5♡", "6♡"} or \
                    set(straight_flush) == {"2♢", "3♢", "4♢", "5♢", "6♢"} or \
                    set(straight_flush) == {"2♣", "3♣", "4♣", "5♣", "6♣"}:
                return hand_ranking.index("Straight Flush")
            elif set(straight_flush) == {"3♠", "4♠", "5♠", "6♠", "7♠"} or \
                    set(straight_flush) == {"3♡", "4♡", "5♡", "6♡", "7♡"} or \
                    set(straight_flush) == {"3♢", "4♢", "5♢", "6♢", "7♢"} or \
                    set(straight_flush) == {"3♣", "4♣", "5♣", "6♣", "7♣"}:
                return hand_ranking.index("Straight Flush")
            elif set(straight_flush) == {"4♠", "5♠", "6♠", "7♠", "8♠"} or \
                    set(straight_flush) == {"4♡", "5♡", "6♡", "7♡", "8♡"} or \
                    set(straight_flush) == {"4♢", "5♢", "6♢", "7♢", "8♢"} or \
                    set(straight_flush) == {"4♣", "5♣", "6♣", "7♣", "8♣"}:
                return hand_ranking.index("Straight Flush")
            elif set(straight_flush) == {"5♠", "6♠", "7♠", "8♠", "9♠"} or \
                    set(straight_flush) == {"5♡", "6♡", "7♡", "8♡", "9♡"} or \
                    set(straight_flush) == {"5♢", "6♢", "7♢", "8♢", "9♢"} or \
                    set(straight_flush) == {"5♣", "6♣", "7♣", "8♣", "9♣"}:
                return hand_ranking.index("Straight Flush")
            elif set(straight_flush) == {"6♠", "7♠", "8♠", "9♠", "10♠"} or \
                    set(straight_flush) == {"6♡", "7♡", "8♡", "9♡", "10♡"} or \
                    set(straight_flush) == {"6♢", "7♢", "8♢", "9♢", "10♢"} or \
                    set(straight_flush) == {"6♣", "7♣", "8♣", "9♣", "10♣"}:
                return hand_ranking.index("Straight Flush")
            elif set(straight_flush) == {"7♠", "8♠", "9♠", "10♠", "J♠"} or \
                    set(straight_flush) == {"7♡", "8♡", "9♡", "10♡", "J♡"} or \
                    set(straight_flush) == {"7♢", "8♢", "9♢", "10♢", "J♢"} or \
                    set(straight_flush) == {"7♣", "8♣", "9♣", "10♣", "J♣"}:
                return hand_ranking.index("Straight Flush")
            elif set(straight_flush) == {"8♠", "9♠", "10♠", "J♠", "Q♠"} or \
                    set(straight_flush) == {"8♡", "9♡", "10♡", "J♡", "Q♡"} or \
                    set(straight_flush) == {"8♢", "9♢", "10♢", "J♢", "Q♢"} or \
                    set(straight_flush) == {"8♣", "9♣", "10♣", "J♣", "Q♣"}:
                return hand_ranking.index("Straight Flush")
            elif set(straight_flush) == {"9♠", "10♠", "J♠", "Q♠", "K♠"} or \
                    set(straight_flush) == {"9♡", "10♡", "J♡", "Q♡", "K♡"} or \
                    set(straight_flush) == {"9♢", "10♢", "J♢", "Q♢", "K♢"} or \
                    set(straight_flush) == {"9♣", "10♣", "J♣", "Q♣", "K♣"}:
                return hand_ranking.index("Straight Flush")
            elif set(straight_flush) == {"10♠", "J♠", "Q♠", "K♠", "A♠"} or \
                    set(straight_flush) == {"10♡", "J♡", "Q♡", "K♡", "A♡"} or \
                    set(straight_flush) == {"10♢", "J♢", "Q♢", "K♢", "A♢"} or \
                    set(straight_flush) == {"10♣", "J♣", "Q♣", "K♣", "A♣"}:
                return hand_ranking.index("Straight Flush")

    # Check for Four of a Kind
    if rank_counts[0][1] >= 4:
        return hand_ranking.index("Four of a Kind")

    # Check for Full House
    if len(rank_counts) >= 2 and rank_counts[0][1] >= 3 and rank_counts[1][1] >= 2:
        return hand_ranking.index("Full House")

    # Check for Flush
    for suit in suits:
        if suits.count(suit) >= 5:
            return hand_ranking.index("Flush")

    # Check for Straight
    if 'A' in ranks:
        straight_ranks = ['A', '2', '3', '4', '5']
    else:
        straight_ranks = sorted(set(ranks), key=lambda x: ranks.index(x))

    for i in range(len(straight_ranks) - 4):
        if straight_ranks[i:i + 5] == ['2', '3', '4', '5', 'A']:
            return hand_ranking.index("Straight")

    # Check for Three of a Kind
    if rank_counts[0][1] >= 3:
        return hand_ranking.index("Three of a Kind")

    # Check for Two Pairs
    if len(rank_counts) >= 2 and rank_counts[0][1] >= 2 and rank_counts[1][1] >= 2:
        return hand_ranking.index("Two Pairs")

    # Check for One Pair
    if rank_counts[0][1] >= 2:
        return hand_ranking.index("One Pair")

    # High Card
    return hand_ranking.index("High Card")
