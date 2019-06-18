import unittest
from app import functions
import nltk

INGREDIENTS = [
    'creme', 'de',
    'grand', 'marnier',
    'chambord', 'raspberry',
    'midori', 'melon',
    'malibu', 'rum',
    '151', 'proof',
    'vanilla', 'ice-cream',
    'dark', 'rum',
    'jack', 'daniels',
    'triple', 'sec',
    'sweet', 'and',
    'blue', 'curacao',
    'sour', 'mix',
    'kahlua', 'baileys',
    'irish', 'cream',
    'absolut', 'citron',
    'peach', 'schnapps',
    'ginger', 'ale',
    'southern', 'comfort',
    'maraschino', 'cherry',
    'baileys', 'irish',
    'sweet', 'vermouth',
    'egg', 'white',
    'heavy', 'cream',
    'dry', 'vermouth',
    'club', 'soda',
    'apricot', 'brandy',
    'sloe', 'gin',
    'blended', 'whiskey',
    'food', 'coloring',
    'whipped', 'cream',
    'red', 'wine',
    'chocolate', 'syrop',
    'powdered', 'sugar',
    'cocoa', 'powder',
    'vanilla', 'extract',
    'lemon-lime', 'soda'
]

nltk.download('punkt')


class TestFunctions(unittest.TestCase):

    def test_find_in_vocab_empty_ingredient_list(self):
        result = functions.find_in_vocab([])

        self.assertEqual(len(result), 0)

    def test_find_in_vocab_creme_de(self):
        result = functions.find_in_vocab(["creme", "de"])

        self.assertEqual(len(result), 1)

    def test_find_in_vocab_vodka_banana(self):
        result = functions.find_in_vocab(["vodka", "banana"])

        self.assertEqual(len(result), 2)

    def test_find_in_vocab_all_conjuctions(self):
        result = functions.find_in_vocab(INGREDIENTS)
        self.assertEqual(len(result), 58)

    def test_get_deduced(self):
        result = functions.get_deduced_ingredients(["vodka", "coca-cola"])
        self.assertEqual(len(result), 6)

if __name__ == '__main__':
    unittest.main()
