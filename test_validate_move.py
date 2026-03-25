from unittest import TestCase
from simple_game import validate_move

mock_board = {
    (0,0): "Mock Description",
    (0,1): "Mock Description",
    (1,0): "Mock Description",
    (1,1): "Mock Description"
}

class Test(TestCase):
    def test_validate_move_with_valid_direction_choice(self):
        mock_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 5,
            "Name": "Doris"
        }
        mock_direction = 2
        self.assertTrue(validate_move(mock_board,mock_character,mock_direction))

    def test_validate_move_with_invalid_direction_choice(self):
        mock_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 5,
            "Name": "Doris"
        }
        mock_direction = 1
        self.assertFalse(validate_move(mock_board, mock_character, mock_direction))

