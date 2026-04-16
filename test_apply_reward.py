from unittest import TestCase
from game import apply_reward

class Test(TestCase):
    def test_apply_reward_level_one(self):
        test_character = {
        "X-coordinate": 0,
        "Y-coordinate": 0,
        "Current HP": 10,
        "Name": "test_name",
        "Rank Title": "Soldado",
        "Rank": 1,
        "XP": 0,
        "inventory" : {}
    }
        apply_reward(test_character)
        self.assertTrue(test_character["XP"] == 2)