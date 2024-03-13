from random import shuffle
from typing import List, Tuple, Union

DECK_OF_CARDS = ((rank, suit)
                 for rank in (*range(2, 11), "Jack", "Queen", "King", "Ace")
                 for suit in ("Diamonds", "Clubs", "Hearts", "Spades")
                 )


def deal_hand_from_deck(deck: List[Tuple[Union[int, str], str]], hand_size: int = 5):
    """Returns the next hand of cards
    This function mutates the deck"""

    num_of_cards = min(len(deck), hand_size)
    print(num_of_cards)
    hand = deck[:num_of_cards]
    deck = deck[num_of_cards:]
    return hand

# game 1
deck = shuffle(list(DECK_OF_CARDS))
first_hand = deal_hand_from_deck(deck)
"""shuffle returns None -> it change object but dont return them, just mutate"""

# game 2
deck2 = list(DECK_OF_CARDS)
shuffle(deck2)
first_hand2 = deal_hand_from_deck(deck2, 2)


