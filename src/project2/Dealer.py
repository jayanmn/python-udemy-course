from src.project2.Hand import Hand


class Dealer:
    name = "Dealer"

    def __init__(self):
        self.hand = Hand()

    def deal(self, card):
        if len(self.hand.cards) == 0:
            card.hidden = True
        self.hand.deal(card)

    def unhide(self):
        for card in self.hand.cards:
            card.hidden = False

    def __str__(self):
        return f"Dealer: \n{self.hand}"
