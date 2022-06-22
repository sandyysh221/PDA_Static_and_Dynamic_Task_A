import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Clubs", 1)
        self.card2 = Card("Hearts", 5)
        self.card3 = Card("Diamonds", 10)

    def test_check_for_ace__true(self):
        result = CardGame.check_for_ace(self, self.card1)
        self.assertEqual(True, result)

    def test_check_for_ace__false(self):
        result = CardGame.check_for_ace(self, self.card2)
        self.assertEqual(False, result)

    def test_highest_card(self):
        result = CardGame.highest_card(self, self.card2, self.card3)
        self.assertEqual(self.card3, result)

    def test_cards_total(self):
        cards = [self.card1, self.card2, self.card3]
        result = CardGame.cards_total(self, cards)
        self.assertEqual("You have a total of 16", result)
