import numpy as np
import matplotlib as mpl

deck = [
    ["As", "Ah", "Ac", "Ad"],  # Aces
    ["Ks", "Kh", "Kc", "Kd"],  # Kings
    ["Qs", "Qh", "Qc", "Qd"],  # Queens
    ["Js", "Jh", "Jc", "Jd"],  # Jacks
    ["10s", "10h", "10c", "10d"],  # Tens
    ["9s", "9h", "9c", "9d"],  # Nines
    ["8s", "8h", "8c", "8d"],  # Eights
    ["7s", "7h", "7c", "7d"],  # Sevens
    ["6s", "6h", "6c", "6d"],  # Sixes
    ["5s", "5h", "5c", "5d"],  # Fives
    ["4s", "4h", "4c", "4d"],  # Fours
    ["3s", "3h", "3c", "3d"],  # Threes
    ["2s", "2h", "2c", "2d"],  # Twos
]
suitedCombos = []  # Initialize an empty list to store the suited combinations
pairCombos = []  # Initialize an empty list to store the pair combinations
offsuitCombos = []  # Initialize an empty list to store the offsuit combinations


def pairComboGenerator():
    for i in range(len(deck)):
        # Iterate over each sublist in the deck

        for j in range(len(deck[i])):
            # Iterate over each card in the current sublist

            for k in range(j + 1, len(deck[i])):
                # Iterate over the remaining cards in the same sublist

                # Create a pair combination by selecting two cards of the same rank
                pairCombos.append([deck[i][j], deck[i][k]])
    return pairCombos

def offsuitComboGenerator():

    for i in range(len(deck)):
        # Iterate over each sublist in the deck

        for j in range(len(deck[i])):
            # Iterate over each card in the current sublist

            for k in range(i + 1, len(deck)):
                # Iterate over the remaining sublists starting from the next one

                for l in range(len(deck[k])):
                    # Iterate over each card in the subsequent sublist

                    if deck[i][j][-1] != deck[k][l][-1]:
                        # Check if the suits of the two cards are different

                        offsuitCombos.append([deck[i][j], deck[k][l]])
                        # Append the offsuit combination of cards to the offsuitCombos list

    return offsuitCombos    

def suitedComboGenerator():
    for i in range(len(deck)):
        # Iterate over each sublist in the deck

        for j in range(len(deck[i])):
            # Iterate over each card in the current sublist

            for k in range(i + 1, len(deck)):
                # Iterate over the subsequent sublists

                for l in range(len(deck[k])):
                    # Iterate over each card in the subsequent sublist

                    if deck[i][j][-1] == deck[k][l][-1]:
                        # Check if the suits of the two cards match

                        suitedCombos.append([deck[i][j], deck[k][l]])
                        # Append the combination of suited cards to the suitedCombos list
    return suitedCombos

def rangeMatrixGenerator():

if __name__ == "__main__":

    suitedComboGenerator()
    print(f'suited combo count: {round(len(suitedCombos)/1326, 3)*100}%')
    pairComboGenerator()
    print(f'pair count:  {len(pairCombos)/1326}')
    offsuitComboGenerator()
    print(f'offsuit count: {len(offsuitCombos)/1326}')

    
