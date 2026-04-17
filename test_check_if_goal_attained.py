from unittest import TestCase
from game import check_if_goal_attained

class Test(TestCase):
    def setUp(self):
        self.rows = 15
        self.columns = 15
    def test_check_if_goal_attained_character_coords_not_14_14(self):
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5, "Name": "Doris"}
        expected = False
        actual = check_if_goal_attained(character, self.rows, self.columns)
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_character_coords_are_14_14(self):
        character = {"X-coordinate": 14, "Y-coordinate": 14, "Current HP": 5, "Name": "Doris"}
        expected = True
        actual = check_if_goal_attained(character, self.rows, self.columns)
        self.assertEqual(expected, actual)

