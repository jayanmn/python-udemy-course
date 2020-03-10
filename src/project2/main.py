# #To play a hand of Blackjack the following steps must be followed:
# 1. Create a deck of 52 cards
from src.project2.BlackJack import BlackJack
from src.project2.Dealer import Dealer
from src.project2.Deck import Deck
from src.project2.Player import Player


def play():
    # Game Play
    # To play a hand of Blackjack the following steps must be followed:
    # 1. Create a deck of 52 cards
    # 2. Shuffle the deck
    card_deck = Deck()
    # print(card_deck)

    # 3. Ask the Player for their bet
    # 4. Make sure that the Player's bet does not exceed their available chips
    max_bet = 10
    player_bet = int(input(f"Enter bet amount(max bet {max_bet}): "))
    while player_bet > max_bet:
        player_bet = int(input(f"Enter bet amount(max bet {max_bet}): "))

    player = Player(player_bet, 10)
    dealer = Dealer()
    blackjack = BlackJack(player, dealer, card_deck)

    # 5. Deal two cards to the Dealer and two cards to the Player
    blackjack.deal()

    # 6. Show only one of the Dealer's cards, the other remains hidden
    print(str(dealer))
    # 7. Show both of the Player's cards
    print(str(player))
    # 8. Ask the Player if they wish to Hit, and take another card
    blackjack.player_hits()

    # 10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or
    # exceeds 17
    if not player.hand.busted():
        blackjack.dealer_turn()

    blackjack.decide_winner()


if __name__ == "__main__":
    while True:
        play()

        # 12. Ask the Player if they'd like to play again
        want_to_play_again = input("Do you want to play again? Y/N : ")
        if want_to_play_again.lower() != "y":
            print("Thanks for playing! See you again.")
            break
