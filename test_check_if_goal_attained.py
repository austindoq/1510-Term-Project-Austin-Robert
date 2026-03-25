from unittest import TestCase
from simple_game import check_if_goal_attained

class Test(TestCase):
    def test_check_if_goal_attained_character_coords_not_4_4(self):
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5, "Name": "Doris"}
        expected = False
        actual = check_if_goal_attained(character)
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_character_coords_are_4_4(self):
        character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 5, "Name": "Doris"}
        expected = True
        actual = check_if_goal_attained(character)
        self.assertEqual(expected, actual)

