"""This initial work is intended to explore the potential relationships between
classes that may be used currently or more likely in the near future. The goal is 
to develop a small demo to simulate a full hand of poker Texas Hold Em with min
6 players to play. 
Author: Anthony Rojas
Date Last Modified: May 1, 2023
 """

from playerHand import*
import math

def main():
    user_playerNumInput = int(input("Enter the number of players:"))
    HandInPlay = HandGenerator(user_playerNumInput)

    print(HandInPlay.dealCards())
    print(HandInPlay.dealBoard())
    print(HandInPlay.getBoard())
    #print(HandInPlay.getPlayerList())


main()