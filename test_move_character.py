from unittest import TestCase
from simple_game import move_character

class Test(TestCase):
    def test_move_character_north(self):
        mock_character = {"X-coordinate": 1,"Y-coordinate": 1,"Current HP": 5,"Name": "Doris"}
        mock_direction = 1
        move_character(mock_character, mock_direction)
        expected = {"X-coordinate": 1,"Y-coordinate": 0,"Current HP": 5,"Name": "Doris"}
        self.assertEqual(expected, mock_character)

    def test_move_character_east(self):
        mock_character = {"X-coordinate": 1,"Y-coordinate": 1,"Current HP": 5,"Name": "Doris"}
        mock_direction = 2
        move_character(mock_character, mock_direction)
        expected = {"X-coordinate": 2,"Y-coordinate": 1,"Current HP": 5,"Name": "Doris"}
        self.assertEqual(expected, mock_character)

    def test_move_character_south(self):
        mock_character = {"X-coordinate": 1,"Y-coordinate": 1,"Current HP": 5,"Name": "Doris"}
        mock_direction = 3
        move_character(mock_character, mock_direction)
        expected = {"X-coordinate": 1,"Y-coordinate": 2,"Current HP": 5,"Name": "Doris"}
        self.assertEqual(expected, mock_character)

    def test_move_character_west(self):
        mock_character = {"X-coordinate": 1,"Y-coordinate": 1,"Current HP": 5,"Name": "Doris"}
        mock_direction = 4
        move_character(mock_character, mock_direction)
        expected = {"X-coordinate": 0,"Y-coordinate": 1,"Current HP": 5,"Name": "Doris"}
        self.assertEqual(expected, mock_character)