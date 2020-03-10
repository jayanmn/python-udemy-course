import random

from src.project2.Card import Card


class Deck:
    play_cards = [("Ace", 1), ("Two", 2), ("Three", 3), ("Four", 4), ("Five", 5), ("Six", 6), ("Seven", 7),
                  ("Eight", 8),
                  ("Nine", 9), ("Ten", 10), ("Jack", 10), ("Queen", 10), ("King", 10)]
    color_set = ["Spade", "Hearts", "Diamond", "Club"]

    def __init__(self):
        self.cards_available = []
        self.reset_card_deck()

    def shuffle_deck(self):
        random.shuffle(self.cards_available)

    def get_card(self):
        self.shuffle_deck()
        return self.cards_available.pop()

    def __str__(self):
        return str(self.play_cards)

    def reset_card_deck(self):
        for i in range(0, 13):
            play_card = self.play_cards[i]
            for shade in self.color_set:
                name = play_card[0]
                value = play_card[1]
                self.cards_available.append(Card(name, value, shade))
