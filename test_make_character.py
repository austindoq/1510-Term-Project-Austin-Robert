from unittest import TestCase, mock
from game import make_character
from unittest.mock import patch

class Test(TestCase):
    #Correct spawn stats are set up on character creation
    @patch("builtins.input", side_effect=["Rob"])
    def test_make_character_dictionary(self, _):
        expected = {
        "X-coordinate": 0,
        "Y-coordinate": 0,
        "Current HP": 10,
        "Name": "Rob",
        "Rank Title": "Soldado",
        "Rank": 1,
        "XP": 0,
        "inventory" : {}
    }
        actual = make_character()
        self.assertEqual(expected, actual)
