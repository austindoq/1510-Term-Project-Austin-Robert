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
        test_enemy_level_1 = {
        "Current HP": 2,
        "XP Dropped": 2,
        "Hit chance": 0.6,
        "stamina": 3
    }
        apply_reward(test_character, test_enemy_level_1)
        self.assertEqual(test_character["XP"], 2)

    def test_apply_xp_reward_level_2_no_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Cabo",
            "Rank": 2,
            "XP": 6,
            "inventory": {}
        }
        test_enemy_level_2 = {
            "Current HP": 2,
            "XP Dropped": 5,
            "Hit chance": 0.6,
            "stamina": 3
        }
        apply_reward(test_character, test_enemy_level_2)
        self.assertEqual(test_character["XP"], 11)

    def test_apply_xp_reward_level_3_no_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Brigada",
            "Rank": 3,
            "XP": 16,
            "inventory": {}
        }
        test_enemy_level_3 = {
            "Current HP": 2,
            "XP Dropped": 10,
            "Hit chance": 0.6,
            "stamina": 3
        }
        apply_reward(test_character, test_enemy_level_3)
        self.assertEqual(test_character["XP"], 26)

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
        test_enemy = {
            "XP Dropped" : 0
        }
        apply_reward(test_character, test_enemy)
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
        test_enemy = {
            "XP Dropped" : 0
        }
        apply_reward(test_character, test_enemy)
        self.assertEqual(test_character["Current HP"], 15 + 1)

    def test_apply_hp_reward_level_2_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Cabo",
            "Rank": 2,
            "XP": 16,
            "inventory": {}
        }
        test_enemy = {
            "XP Dropped" : 0
        }
        apply_reward(test_character, test_enemy)
        self.assertEqual(test_character["Current HP"], 20 + 1)

    def test_apply_hp_reward_level_3_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Brigada",
            "Rank": 3,
            "XP": 31,
            "inventory": {}
        }
        test_enemy = {
            "XP Dropped" : 0
        }
        apply_reward(test_character, test_enemy)
        self.assertEqual(test_character["Current HP"], 25 + 1)

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
        test_enemy = {
            "XP Dropped" : 0
        }
        apply_reward(test_character, test_enemy)
        self.assertEqual(test_character["Rank Title"], "Cabo")

    def test_apply_rank_title_reward_level_2_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Cabo",
            "Rank": 2,
            "XP": 16,
            "inventory": {}
        }
        test_enemy = {
            "XP Dropped" : 0
        }
        apply_reward(test_character, test_enemy)
        self.assertEqual(test_character["Rank Title"], "Brigada")


    def test_apply_rank_title_reward_level_3_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Brigada",
            "Rank": 3,
            "XP": 31,
            "inventory": {}
        }
        test_enemy = {
            "XP Dropped" : 0
        }
        apply_reward(test_character, test_enemy)
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
        test_enemy = {
            "XP Dropped" : 0
        }
        apply_reward(test_character, test_enemy)
        self.assertEqual(test_character["Rank"], 2)

    def test_apply_rank_increase_reward_level_2_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Cabo",
            "Rank": 2,
            "XP": 16,
            "inventory": {}
        }
        test_enemy = {
            "XP Dropped" : 0
        }
        apply_reward(test_character, test_enemy)
        self.assertEqual(test_character["Rank"], 3)

    def test_apply_rank_increase_reward_level_3_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Brigada",
            "Rank": 3,
            "XP": 31,
            "inventory": {}
        }
        test_enemy = {
            "XP Dropped": 0
        }
        apply_reward(test_character, test_enemy)
        self.assertEqual(test_character["Rank"], 4)


