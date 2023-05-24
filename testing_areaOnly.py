suited_Aces = []

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

for i in range(len(deck[0])):  # Iterate across each element of the first sublist
    for j in range(1, len(deck)):  # Iterate across the remaining sublists
        for k in range(len(deck[j])):  # Iterate across each element of the current sublist
            if deck[0][i][-1] == deck[j][k][-1]:  # Check if the suits match
                suited_Aces.append([deck[0][i], deck[j][k]])

print(suited_Aces)
