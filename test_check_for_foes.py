from unittest import TestCase
from unittest.mock import patch
from game import check_for_foes

class Test(TestCase):
    def setUp(self):
        self.test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Soldado",
            "Rank": 1,
            "XP": 0,
            "inventory": {}
        }

    @patch('random.randint', return_value=1)
    def test_check_for_foes_false_one(self, _):
        expected = False
        actual = check_for_foes(self.test_character)
        self.assertEqual(expected,actual)

    @patch('random.randint', return_value=2)
    def test_check_for_foes_false_two(self, _):
        expected = False
        actual = check_for_foes(self.test_character)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_check_for_foes_false_three(self, _):
        expected = True
        actual = check_for_foes(self.test_character)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=4)
    def test_check_for_foes_true_four(self, _):
        expected = False
        actual = check_for_foes(self.test_character)
        self.assertEqual(expected, actual)
