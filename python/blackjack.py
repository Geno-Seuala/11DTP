import random

def card_deck():
    """ 
    Generates a deck of 52 cards 
    
    Arguments:
    
    Returns: a list containing every card in a standard deck
    """
    values = ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['Hearts','Spades','Clubs','Diamonds']
    deck = []
    for suit in suits:
        for value in values:
            deck.append(value + " of " + suit)
    return deck

deck = card_deck()

def dealerdraw():
    dealercards = []
    for num in range(2):
        card = (random.choice(deck))
        dealercards.append(card)
        deck.remove(card)
    return dealercards



        
