from unittest import TestCase
from unittest.mock import patch
from simple_game import guessing_game

class Test(TestCase):
    @patch('random.randint', return_value=3)
    @patch('builtins.input', side_effect=["3"])
    def test_guessing_game_correct_guess(self,_, __):
        mock_character = {"X-coordinate": 1,"Y-coordinate": 1,"Current HP": 5,"Name": "Doris"}
        guessing_game(mock_character)
        expected = {"X-coordinate": 1,"Y-coordinate": 1,"Current HP": 5,"Name": "Doris"}
        self.assertEqual(expected, mock_character)

    @patch('random.randint', return_value=3)
    @patch('builtins.input', side_effect=["2", "3"])
    def test_guessing_game_incorrect_guess_then_correct(self, _, __):
        mock_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Name": "Doris"}
        guessing_game(mock_character)
        expected = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 4, "Name": "Doris"}
        self.assertEqual(expected, mock_character)

    @patch('random.randint', return_value=3)
    @patch('builtins.input', side_effect=["2", "4", "1", "1", "3"])
    def test_guessing_game_incorrect_guess_until_1hp_then_correct(self, _, __):
        mock_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Name": "Doris"}
        guessing_game(mock_character)
        expected = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 1, "Name": "Doris"}
        self.assertEqual(expected, mock_character)

    @patch('random.randint', return_value=3)
    @patch('builtins.input', side_effect=["2","1","5","4","2"])
    def test_guessing_game_incorrect_guess_until_dead(self, _, __):
        mock_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Name": "Doris"}
        guessing_game(mock_character)
        expected = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 0, "Name": "Doris"}
        self.assertEqual(expected, mock_character)

    @patch('random.randint', return_value=3)
    @patch('builtins.input', side_effect=["word", "3"])
    def test_guessing_game_guess_non_integer_first_then_correct(self, _, __):
        mock_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Name": "Doris"}
        guessing_game(mock_character)
        expected = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Name": "Doris"}
        self.assertEqual(expected, mock_character)







