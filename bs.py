class Game:
    def __init__(self):
        self.playerList = ["Player1", "Player2", "Player3", "Player4"]
        self.deck = ['A♠', 'K♠', 'Q♠', 'J♠', '10♠', '9♠', '8♠', '7♠', '6♠', '5♠', '4♠', '3♠', '2♠',
                     'A♥', 'K♥', 'Q♥', 'J♥', '10♥', '9♥', '8♥', '7♥', '6♥', '5♥', '4♥', '3♥', '2♥',
                     'A♦', 'K♦', 'Q♦', 'J♦', '10♦', '9♦', '8♦', '7♦', '6♦', '5♦', '4♦', '3♦', '2♦',
                     'A♣', 'K♣', 'Q♣', 'J♣', '10♣', '9♣', '8♣', '7♣', '6♣', '5♣', '4♣', '3♣', '2♣']
        self.playerHandsDealt = {}

    def dealPreFlop(self):
        """Deal cards to players"""
        numCards = 2
        for player in self.playerList:
            self.playerHandsDealt[player] = [self.deck.pop() for _ in range(numCards)]
        print(f'The remaining cards are: {len(self.deck)}/52')
        return self.playerHandsDealt

# Create an instance of the Game class
game = Game()

# Call the dealPreFlop function
dealtHands = game.dealPreFlop()

# Print the dealt hands for each player
for player, cards in dealtHands.items():
    print(f"Player {player} was dealt: {cards}")
