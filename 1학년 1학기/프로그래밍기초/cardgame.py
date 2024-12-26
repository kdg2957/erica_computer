def hit(deck):
    if deck == []:
        deck = fresh_deck()
        
    return (deck[0], deck[1:])

def show_cards(cards, massage):
    print(massage)
    for card in cards:
        print(' ', card[0], card[1])

def more(massage):
    answer = input(massage)
    while not (answer in ['y','n']):
        answer = input(massage)
    return answer == 'y'