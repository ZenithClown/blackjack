# -*- encoding: utf-8 -*-

"""Play the CLI/GUI Version of the Black Jack Game"""

from blackjack import (
        Card,
        Deck,
        Hand
    )

def command_line_interface():
    """Defines the CLI (Command Line Interface) of the Game"""
    deck = Deck()

    playerHand = Hand()
    dealerHand = Hand(dealer = True)

    for _ in range(2):
        playerHand.addCard(deck.deal())
        dealerHand.addCard(deck.deal())

    print(playerHand.showHand())
    print(dealerHand.showHand())

    print(f"Dealer : {dealerHand.getValue} | Player : {playerHand.getValue}")


if __name__ == '__main__':
    # Choose Game Type, if y = CLI else GUI | Defaults to CLI
    gameType = input("Play Game in CLI (Y/n) : ").lower() or "y"

    if gameType in ["y", "yes"]:
        command_line_interface()