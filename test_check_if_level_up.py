from unittest import TestCase
from game import check_if_level_up

class Test(TestCase):
    #No level up
    def test_check_if_level_up_no_level_up_no_change(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 6,
            "Name": "test_name",
            "Rank Title": "Soldado",
            "Rank": 1,
            "XP": 2,
            "inventory": {}
        }
        test_func_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 6,
            "Name": "test_name",
            "Rank Title": "Soldado",
            "Rank": 1,
            "XP": 2,
            "inventory": {}
        }
        check_if_level_up(test_func_character)
        self.assertEqual(test_character,test_func_character)

    #Level Up changes applied
    def test_apply_hp_reward_level_one_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 6,
            "Name": "test_name",
            "Rank Title": "Soldado",
            "Rank": 1,
            "XP": 6,
            "inventory": {}
        }
        check_if_level_up(test_character)
        self.assertEqual(test_character["Current HP"], 11)

    def test_apply_hp_reward_level_two_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 6,
            "Name": "test_name",
            "Rank Title": "Cabo",
            "Rank": 2,
            "XP": 16,
            "inventory": {}
        }
        check_if_level_up(test_character)
        self.assertEqual(test_character["Current HP"], 16)

    def test_apply_hp_reward_level_three_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 6,
            "Name": "test_name",
            "Rank Title": "Brigada",
            "Rank": 3,
            "XP": 31,
            "inventory": {}
        }
        check_if_level_up(test_character)
        self.assertEqual(test_character["Current HP"], 21)

#Level Up changes applied
    def test_apply_rank_title_reward_level_one_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 6,
            "Name": "test_name",
            "Rank Title": "Soldado",
            "Rank": 1,
            "XP": 6,
            "inventory": {}
        }
        check_if_level_up(test_character)
        self.assertEqual(test_character["Rank Title"], "Cabo")

    def test_apply_rank_title_reward_level_two_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 6,
            "Name": "test_name",
            "Rank Title": "Cabo",
            "Rank": 2,
            "XP": 16,
            "inventory": {}
        }
        check_if_level_up(test_character)
        self.assertEqual(test_character["Rank Title"], "Brigada")

    def test_apply_rank_title_reward_level_three_on_level_up(self):
        test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 6,
            "Name": "test_name",
            "Rank Title": "Brigada",
            "Rank": 3,
            "XP": 31,
            "inventory": {}
        }
        check_if_level_up(test_character)
        self.assertEqual(test_character["Rank Title"], "Capitán")

    # Rank increase on level up
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
        check_if_level_up(test_character)
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
        check_if_level_up(test_character)
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
        check_if_level_up(test_character)
        self.assertEqual(test_character["Rank"], 4)


