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

    def card_value(self, hand_has_ace : bool, hand_total_value : int or float) -> int:
        """Sets the Value of the Card and Returns Integer Value"""

        if self.value.isnumeric():
            return int(self.value)

        elif self.card.value == "A":
            # set the value of A as per Game Rules
            if hand_has_ace and (hand_total_value >= 21):
                return 1
            else:
                return 11

        else:
            return 10 # K, Q, J each has a value of 10
    

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

class Hand:
    """Class to Create an Object of the Player's Hand. Currently,
    only two player mode is supported, i.e. one is the Dealer and
    the other is set as the player.

    :type  dealer : bool
    :param dealer : If  the player is the dealer, or Ordinary Player?
                    Defaults to False, i.e. the Player.
    """

    def __init__(self, dealer : bool = False):
        self.dealer = dealer

        # now each player will have their own cards,
        # each card will have its total value
        self.cards = [] # list of all the Cards
        self.value = 0  # Initially the Value is Zero

        # checks if the card is an ace
        self.has_ace = False

    def addCard(self, card):
        """Adds a Card from the Pile (deck) and Assigns it to the Player's Hand"""

        self.cards.append(card) # adds the new Card

        if card.value == "A":
            self.has_ace = True

        self.value += card.card_value(
                hand_has_ace     = self.has_ace,
                hand_total_value = self.value
            )

    @property
    def getValue(self) -> int:
        """Returns the Total Value of the Hand"""

        return self.value

    def showHand(self):
        if self.dealer:
            return ["hidden", self.cards[1]]
        else:
            return [card for card in self.cards]
    