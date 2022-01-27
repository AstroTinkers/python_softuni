card_deck = input()
shuffles = int(input())
shuffled_deck = card_deck.split(" ")
deck_3 = []
for i in range(shuffles):
    deck_1 = shuffled_deck[:len(shuffled_deck) // 2]
    deck_2 = shuffled_deck[len(shuffled_deck) // 2:]
    deck_3 += [i for i in deck_1[i]]
    deck_3 += [i for i in deck_2[i]]
    shuffled_deck = deck_3

print(shuffled_deck)
