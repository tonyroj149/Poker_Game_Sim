"""These classes should be enough to generate players and corresponding hands.
Author: Anthony Rojas
Date Last Modified: May 1, 2023
"""

import random
# This class represents a poker player and generates a hand based on the remaining cards in the deck
class pokerPlayer:
    
    def __init__(self, name, init_Stack = None):
        self.name = name
        self.firstCard = ''  # First card in hand
        self.secondCard = ''  # Second card in hand
        self.stackSize = init_Stack
        self.frequencies = playerFrequencies()
 
    def getCards(self):
        """Return the player's hand"""
        return [self.firstCard, self.secondCard]
    
    def getName(self):
        """Return the player's name"""
        return self.name
    
    def getStackSize(self):
        return self.stackSize
    
    def setFirstCard(self, card):
        """Set the player's first card"""
        self.firstCard = card

    def setSecondCard(self, card):
        """Set the player's second card"""
        self.secondCard = card   

    def setStackSize(self, value):
        self.stackSize += value        

class playerFrequencies:
    """Class to represent player frequencies"""
    def __init__(self):
        self.VPIP = random.uniform(5, 45)  # Voluntarily Put In Pot (VPIP)
        self.PFR = random.uniform(10, 30)  # Pre-Flop Raise (PFR)
        self.THREE_BET_PERCENTAGE = random.uniform(5, 15)  # 3-Bet Percentage
        self.FOLD_To_3BET = random.uniform(35, 50)  # Fold to 3-Bet Percentage 
    
    def get_VPIP(self):
        return self.VPIP
      
    def get_PFR(self):
        return self.PFR
    
    def get_THREE_BET_PERCENTAGE(self):
        return self.THREE_BET_PERCENTAGE
    
    def get_FOLD_TO_THREE_BET(self):
        return self.FOLD_To_3BET     
       
class HandGenerator:
    """Class to generate player hands"""
    def __init__(self, numPlayers):
        self.numPlayers = numPlayers
        self.player_dict = {i+1: f'Player {i+1}' for i, x in enumerate(range(self.numPlayers))}
        self.playerHandsDealt = []  # List to store player hands
        self.burnCards = []  # List to store burn cards
        self.hand_Board = []  # List to store community cards on the board
        self.muck = []  # List to store folded cards
        self.deck = ["As", "Ks", "Qs", "Js", "Ts", "9s", "8s", "7s", "6s", "5s", "4s", "3s", "2s",
                     "Ah", "Kh", "Qh", "Jh", "Th", "9h", "8h", "7h", "6h", "5h", "4h", "3h", "2h",
                     "Ac", "Kc", "Qc", "Jc", "Tc", "9c", "8c", "7c", "6c", "5c", "4c", "3c", "2c",
                     "Ad", "Kd", "Qd", "Jd", "Td", "9d", "8d", "7d", "6d", "5d", "4d", "3d", "2d"]  # Deck of cards
        self.Sorted_deck = [["As", "Ah", "Ac", "Ad"], ["Ts", "Th", "Tc", "Td"], ["9s", "9h", "9c", "9d"],
                            ["8s", "8h", "8c", "8d"], ["7s", "7h", "7c", "7d"], ["6s", "6h", "6c", "6d"],
                            ["5s", "5h", "5c", "5d"], ["4s", "4h", "4c", "4d"], ["3s", "3h", "3c", "3d"],
                            ["2s", "2h", "2c", "2d"]]  # Sorted deck for evaluating hands
        
        random.shuffle(self.deck)  # Shuffle the deck of cards

    def getnumPlayers(self):
        """Return the number of players"""
        return f'There are {self.numPlayers} playing'
    
    def getPlayerList(self):
        """Return the list of player names"""
        return f'Player list: {self.playerList}'
    
    def dealPreFlop(self):
        """Deal cards to players"""
        numCards = 2
        for player_number, player_name in self.player_dict.items():
            self.playerHandsDealt.append((player_number, [self.deck.pop() for _ in range(numCards)]))
        print(f'The remaining cards are: {len(self.deck)}/52')
        return self.playerHandsDealt


    def dealFlop(self):
        """Deal community cards to the board"""
        FLOP_CARDS_NUM = 3
    
        self.burnCards.append(self.deck.pop())
        FLOP_CARDS = [self.deck.pop() for _ in range(FLOP_CARDS_NUM)]
        print(f'The remaining cards are: {len(self.deck)}/52')
        self.hand_Board.append(FLOP_CARDS)
        return FLOP_CARDS

    def dealTurn(self):
        TURN_CARD_NUM = 1
        self.burnCards.append(self.deck.pop())
        TURN_CARD = [self.deck.pop() for _ in range(TURN_CARD_NUM)]
        print(f'The remaining cards are: {len(self.deck)}/52')
        self.hand_Board.append(TURN_CARD)
        return TURN_CARD

    def dealRiver(self):
        RIVER_CARD_NUM = 1
        self.burnCards.append(self.deck.pop())
        RIVER_CARD = [self.deck.pop() for _ in range(RIVER_CARD_NUM)]
        print(f'The remaining cards are: {len(self.deck)}/52')
        self.hand_Board.append(RIVER_CARD)

        return RIVER_CARD
    
    def getBoard(self):
        """Return the community cards on the board"""
        return self.hand_Board
    
    def getBurnCards(self):
        return self.burnCards
    
    def getRemainingCards(self):
        return self.deck