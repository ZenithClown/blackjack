# -*- encoding: utf-8 -*-

"""Play the CLI/GUI Version of the Black Jack Game"""

import shutil

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

    playing = True
    num_cards_to_draw = 2

    while playing:
        for _ in range(num_cards_to_draw):
            playerHand.addCard(deck.deal())
            dealerHand.addCard(deck.deal())

        num_cards_to_draw = 1 # after 1st iter, draw single card each time "stick"
        print(f"Player Cards [{playerHand.getValue}] :\n{playerHand.showHand()}")
        print(f"Dealer Cards [{dealerHand.getValue}] :\n{dealerHand.showHand()}")

        # check if black jack obtained
        for p, msg in zip([playerHand, dealerHand], ["Player", "Dealer"]):
            if p.is_blackjack:
                print(f"{msg} WINS!")
                playing = False
                break

        wager = input("Choose [Hit/Stick] : ").lower() # should draw more cards?
        while wager not in ["h", "s", "hit", "stick"]:
            wager = input("Please Enter 'Hit' or 'Stick' (or H/S) : ").lower()

        if wager not in ["h", "hit"]:
            playing = False

    # find the winning player
    if playerHand.getValue > dealerHand.getValue:
        print("Player WINS!")
    elif playerHand.getValue < dealerHand.getValue:
        print("Dealer WINS!")
    else:
        print("Match ended in a DRAW!")


if __name__ == '__main__':
    # prints messages in the middle of the screed
    columns = shutil.get_terminal_size().columns
    print("*** Welcome to CLI/GUI Black Jack (21) Game ***".center(columns))

    # Choose Game Type, if y = CLI else GUI | Defaults to CLI
    gameType = input("Play Game in CLI (Y/n) [yes]: ").lower() or "y"

    if gameType in ["y", "yes"]:
        print("*** Starting CLI Game Play ***".center(columns))
        command_line_interface()