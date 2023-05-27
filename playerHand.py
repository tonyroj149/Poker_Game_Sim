"""These classes should be enough to generate a players and corresponding hands.
Author: Anthony Rojas
Date Last Modified: May 1, 2023
 """
import random
import pyglet

#This class will generate a hand for each player based on the remaining cards in the deck
class pokerPlayer: 
    playerIcon = pyglet.image('playerIcon.png')
    
    def __init__(self, name , position):
        self.name = name
        self.position = position
        self.image = pyglet.image.load('')
        self.sprite = pyglet.sprite.Sprite(self.image)
        self.firstCard = ''
        self.secondCard = ''
 
    def getCards(self):
        return [self.firstCard, self.secondCard]
    
    def getName(self):
        return self.playerName
    
    def setFirstCard(self, card):
        self.firstCard = card

    def setSecondCard(self, card):
        self.secondCard = card    
    
class playerFrequencies:

    def __init__(self):
        self.VPIP = random.uniform(5,45)
        self.PFR =random.uniform(10,30)
        self.THREE_BET_PERCENTAGE = random.uniform(5, 15)
        self.FOLD_To_3BET= random.uniform(35,50)   
            
class HandGenerator:
    def __init__(self, numPlayers):
        self.numPlayers = numPlayers
        self.playerList = [f'Player: {pokerPlayer(x).getName()}' for x in range(1,self.numPlayers +1)]
        self.playerHandsDealt = []
        self.burnCards = []
        self.hand_Board = []
        self.muck = []
        self.deck = ["As", "Ks", "Qs", "Js", "10s", "9s", "8s", "7s", "6s", "5s", "4s", "3s", "2s",
        "Ah", "Kh", "Qh", "Jh", "10h", "9h", "8h", "7h", "6h", "5h", "4h", "3h", "2h",
        "Ac", "Kc", "Qc", "Jc", "10c", "9c", "8c", "7c", "6c", "5c", "4c", "3c", "2c",
        "Ad", "Kd", "Qd", "Jd", "10d", "9d", "8d", "7d", "6d", "5d", "4d", "3d", "2d"]
        self.Sorted_deck = [["As", "Ah", "Ac", "Ad"],  ["10s", "10h", "10c", "10d"], ["9s", "9h", "9c", "9d"],
                     ["8s", "8h", "8c", "8d"], ["7s", "7h", "7c", "7d"],  ["6s", "6h", "6c", "6d"], 
                     ["5s", "5h", "5c", "5d"],  ["4s", "4h", "4c", "4d"],  ["3s", "3h", "3c", "3d"], 
                     ["2s", "2h", "2c", "2d"]]
        


        random.shuffle(self.deck)
        

    def getnumPlayers(self):
        return f'There are {self.numPlayers} playing'
    
    def getPlayerList(self):
        return f'Player list: {self.playerList}'
    
    def dealCards(self):
        numCards = 2
        for player in self.playerList:
            self.playerHandsDealt[player] = [self.deck.pop() for _ in range(numCards)]
        print(f'The remaining cards are: {len(self.deck)}/52')
        return self.playerHandsDealt

    def dealBoard(self):
        FLOP_CARDS_NUM = 3
        TURN_CARD_NUM = 1
        RIVER_CARD_NUM = 1
        
        self.burnCards.append(self.deck.pop())
        FLOP_CARDS = [self.deck.pop() for _ in range(FLOP_CARDS_NUM)]
        print(f'The remaining cards are: {len(self.deck)}/52')
        self.hand_Board.append(FLOP_CARDS)

        self.burnCards.append(self.deck.pop())
        TURN_CARD = [self.deck.pop() for _ in range(TURN_CARD_NUM)]
        print(f'The remaining cards are: {len(self.deck)}/52')
        self.hand_Board.append(TURN_CARD)
        
        self.burnCards.append(self.deck.pop())
        RIVER_CARD = [self.deck.pop() for _ in range(RIVER_CARD_NUM)]
        print(f'The remaining cards are: {len(self.deck)}/52')
        self.hand_Board.append(RIVER_CARD)

        return self.hand_Board
    
    def getBoard(self):
        return  self.hand_Board


        





        
        

