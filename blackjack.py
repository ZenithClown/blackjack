# -*- encoding: utf-8 -*-

"""Black Jack (21) Game in CLI Version is Developed, and will serve
as a Stand Alone Version - if CLI is Preffered. The GUI Version is
developed Seperately, and all the Necessary functions and Methods are
imported from this."""

import random

class Card:
    """The Card Class Creates an Object of Each Cards in a Deck
    and if the GUI is required, then additionally each set of cards
    are associated with their respective Card Image.

    :type  suit : str
    :param suit : Name of the suit
                  (i.e. hearts, spades, diamond, or clubs).

    :type  value : str
    :param value : Value of the Card
                   (i.e. A, 1, 2, ..., 9, J, Q, or K)
    """

    def __init__(self, suit : str, value : str):
        self.suit  = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    """A Typical Card Deck comprises of 52 Cards,
    and this methods creates an instance of all the cards
    using :class:`Card` and performs basic deck operations
    like shuffling and dealing of cards.
    """

    def __init__(self):
        self.cards = [Card(suit, value)
            for suit in ["Spades", "Clubs", "Hearts", "Diamonds"]
            for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        ]

    def shuffle(self):
        """Function to Shuffle all the Cards in the Deck"""

        if len(self.cards) > 1 : random.shuffle(self.cards)

    def deal(self, shuffle_deck : bool = True):
        """Deals a Random Card from the Deck after Shuffling the Deck
        
        :type  shuffle_deck : bool
        :param shuffle_deck : To Shuffle the Deck before Drawing a Card? Defaults
                              to True.
        """

        if len(self.cards) > 1:
            if shuffle_deck:
                self.shuffle() # shuffles the deck

            return self.cards.pop(0)