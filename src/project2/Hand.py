class Hand:
    def __init__(self):
        self.cards = []
        self.total = 0

    def deal(self, card):
        value = card.value
        if card.name.lower() == "ace":
            ace_value = None
            while ace_value not in [1, 11]:
                ace_value = int(input("You got an ACE. Do you want it to be 11 or 1? "))
            value = ace_value

        self.total += value
        self.cards.append(card)

    def busted(self):
        return self.total > 21

    def show(self):
        for card in self.cards:
            print(card)

    def hit(self, card_deck):
        card = card_deck.get_card()

    def __str__(self):
        hand_str = ""
        count = 1
        for card in self.cards:
            hand_str += f"Card{count} -> {card}\n"
            count += 1

        hand_str += f"Total: {self.total}\n"
        return hand_str
