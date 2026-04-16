from unittest import TestCase
from game import apply_reward

class Test(TestCase):
    # XP gain without level up
    def test_apply_xp_reward_level_one_no_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Soldado",
            "Rank": 1,
            "XP": 0,
            "inventory": {}
        }
        apply_reward(test_character)
        self.assertEqual(test_character["XP"], 2)

    def test_apply_xp_reward_level_2_no_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Soldado",
            "Rank": 2,
            "XP": 6,
            "inventory": {}
        }
        apply_reward(test_character)
        self.assertEqual(test_character["XP"], 10)

    def test_apply_xp_reward_level_3_no_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Soldado",
            "Rank": 3,
            "XP": 15,
            "inventory": {}
        }
        apply_reward(test_character)
        self.assertEqual(test_character["XP"], 23)

    # HP gain without level up
    def test_apply_hp_reward_no_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Soldado",
            "Rank": 1,
            "XP": 0,
            "inventory": {}
        }
        apply_reward(test_character)
        self.assertEqual(test_character["Current HP"], 11)

    # HP gain with level up reward
    def test_apply_hp_reward_level_one_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Soldado",
            "Rank": 1,
            "XP": 6,
            "inventory": {}
        }
        apply_reward(test_character)
        self.assertEqual(test_character["Current HP"], 21)

    def test_apply_hp_reward_level_2_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Cabo",
            "Rank": 2,
            "XP": 15,
            "inventory": {}
        }
        apply_reward(test_character)
        self.assertEqual(test_character["Current HP"], 21)

    #Rank title changes on level up
    def test_apply_rank_title_reward_level_1_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Soldado",
            "Rank": 1,
            "XP": 6,
            "inventory": {}
        }
        apply_reward(test_character)
        self.assertEqual(test_character["Rank Title"], "Cabo")

    def test_apply_rank_title_reward_level_2_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Cabo",
            "Rank": 2,
            "XP": 15,
            "inventory": {}
        }
        apply_reward(test_character)
        self.assertEqual(test_character["Rank Title"], "Capitán")

    #Rank increase on level up
    def test_apply_rank_increase_reward_level_1_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Soldado",
            "Rank": 1,
            "XP": 6,
            "inventory": {}
        }
        apply_reward(test_character)
        self.assertEqual(test_character["Rank"], 2)

    def test_apply_rank_increase_reward_level_2_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Cabo",
            "Rank": 2,
            "XP": 15,
            "inventory": {}
        }
        apply_reward(test_character)
        self.assertEqual(test_character["Rank"], 3)


