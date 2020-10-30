# -*- encoding: utf-8 -*-

"""Play the CLI/GUI Version of the Black Jack Game"""

import shutil

from blackjack import (
        Card,
        Deck,
        Hand
    )

class GameComplete(Exception):
    """Notifies, if the Game is Completed - when player has Received Black-Jack"""

    pass

def get_winning_player(player_value : int, dealer_value : int) -> str:
    """Find the Winning Player"""

    if (player_value > 21) and (dealer_value > 21):
        return "Match ended in a DRAW!"
    elif player_value > 21:
        return "Dealer WINS!"
    elif dealer_value > 21:
        return "Player WINS!"
    else:
        if player_value > dealer_value:
            return "Player WINS!"

    return "Dealer WINS!"


def command_line_interface():
    """Defines the CLI (Command Line Interface) of the Game"""
    deck = Deck()

    playerHand = Hand()
    dealerHand = Hand(dealer = True)

    playing = True
    num_cards_to_draw = 2

    try:
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
                    raise GameComplete

            wager = input("Choose [Hit/Stick] : ").lower() # should draw more cards?
            while wager not in ["h", "s", "hit", "stick"]:
                wager = input("Please Enter 'Hit' or 'Stick' (or H/S) : ").lower()

            if wager not in ["h", "hit"]:
                playing = False

        # find the winning player
        print(get_winning_player(playerHand.getValue, dealerHand.getValue))
    except GameComplete:
        pass


if __name__ == '__main__':
    # prints messages in the middle of the screed
    columns = shutil.get_terminal_size().columns
    print("*** Welcome to CLI/GUI Black Jack (21) Game ***".center(columns))

    # Choose Game Type, if y = CLI else GUI | Defaults to CLI
    gameType = input("Play Game in CLI (Y/n) [yes]: ").lower() or "y"

    if gameType in ["y", "yes"]:
        print("*** Starting CLI Game Play ***".center(columns))
        command_line_interface()