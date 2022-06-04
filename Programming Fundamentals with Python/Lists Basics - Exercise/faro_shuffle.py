deck_of_cards = input().split(" ")
shuffle = int(input())

deck_one = []
deck_two = []

for _ in range(shuffle):
    for card in range(len(deck_of_cards)):
        if card < len(deck_of_cards) / 2:
            deck_one.append(deck_of_cards[card])
        else:
            deck_two.append(deck_of_cards[card])

    deck_of_cards = []

    for i in range(len(deck_one)):
        deck_of_cards.append(deck_one[i])
        deck_of_cards.append(deck_two[i])
    deck_one = []
    deck_two = []

print(deck_of_cards)

