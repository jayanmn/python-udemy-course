class BlackJack:
    def __init__(self, player, dealer, card_deck):
        self.dealer = dealer
        self.player = player
        self.card_deck = card_deck

    def decide_winner(self):
        print('------------------------------------')
        print(f"Player's total {self.player.hand.total}")
        print('------------------------------------')
        print(f"Dealer's total {self.dealer.hand.total}")
        print('------------------------------------')

        winner = None
        # If the player "busts"; the player loses, even if the dealer also exceeds 21.
        if self.player.hand.busted():
            winner = self.dealer
        elif self.dealer.hand.busted():  # If the dealer "busts" and the player does not; player wins.
            winner = self.player
        elif self.dealer.hand.total < self.player.hand.total:
            # If the player attains a hand higher than the dealer and does not bust; the player wins.
            winner = self.player
        elif self.dealer.hand.total > self.player.hand.total:
            winner = self.dealer

        print(f"{winner.name} wins")

    def dealer_turn(self):
        print("Dealer's turn to hit")
        while self.dealer.hand.total <= 17:
            self.dealer.hand.deal(self.card_deck.get_card())

        self.dealer.unhide()
        if self.dealer.hand.busted():
            print("Dealer busted")

    def player_hits(self):
        while True:
            want_to_hit = input("Do you want to hit? Y/N: ")
            if want_to_hit.lower() == 'y':
                self.player.hand.deal(self.card_deck.get_card())
                print(f"Player total: {self.player.hand.total}")
            else:
                break

            # 9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
            if self.player.hand.busted():
                print("Player busted")
                break

    def deal(self):
        self.player.deal(self.card_deck.get_card())
        self.player.deal(self.card_deck.get_card())
        self.dealer.deal(self.card_deck.get_card())
        self.dealer.deal(self.card_deck.get_card())
