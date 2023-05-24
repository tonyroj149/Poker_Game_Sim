

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

def suitedComboGenerator():
    suited_Combos = []

    for i in range(len(deck)):
        for j in range(len(deck[i])):
            # Iterate over each card in the current sublist

            for k in range(i+1, len(deck)):
                # Start from i+1 to avoid duplicates and prevent comparing with itself

                for l in range(len(deck[k])):
                    # Iterate over each card in the subsequent sublist

                    if deck[i][j][-1] == deck[k][l][-1]:
                        # Check if the suits of the two cards match

                        suited_Combos.append([deck[i][j], deck[k][l]])
                        # Append the combination of suited cards to the suited_Aces list


print(suited_Combos)
print(f'The suited combos total: {len(suited_Aces)}') 