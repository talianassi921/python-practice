import unittest
from deck import Card
from deck import Deck

class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card()
        
class DeckTests(unittest.TestCase):
    def test_count(self):
        """should return the cards remaining in the deck """
        self.assertEqual(count(self), 52)
        
if __name__ == "__main__":
    unittest.main()