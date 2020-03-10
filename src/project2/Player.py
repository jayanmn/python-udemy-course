from src.project2.Hand import Hand


class Player:
    name = "Player"

    def __init__(self, bet, max_bet):
        self.bet = bet
        self.max_bet = max_bet
        self.hand = Hand()

    def deal(self, card):
        self.hand.deal(card)

    def place_bet(self, bet):
        if bet > (self.max_bet - self.bet):
            print("Sorry you don't have sufficient chips to bet")
        else:
            self.bet += bet

    def stand(self):
        # I don't know what to do here
        pass

    def __str__(self):
        return f"Player: \n{self.hand}"
