import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cardgame1 = CardGame()
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Hearts", 5)
    
    def test_cardgame_check_for_ace(self):
        self.assertEqual(True, self.cardgame1.check_for_ace(self.card1))
    
    def test_cardgame_return_highest_card(self):
        self.assertEqual(self.card1, self.cardgame1.highest_card(self.card1, self.card2))
    
    def test_cardgame_total_cards(self):
        cards = [self.card1, self.card2]
        self.assertEqual("You have a total of 2", self.cardgame1.cards_total(cards))
