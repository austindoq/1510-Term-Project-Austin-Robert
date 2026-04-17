from unittest import TestCase
from game import print_battle_stats
from unittest.mock import patch
from io import StringIO

class Test(TestCase):
    def setUp(self):
        self.test_character = {
            "X-coordinate": 0,
            "Y-coordinate": 0,
            "Current HP": 10,
            "Name": "test_name",
            "Rank Title": "Soldado",
            "Rank": 1,
            "XP": 0,
            "inventory": {}
        }
        self.test_enemy = {
            "Current HP": 2,
            "XP Dropped": 2,
            "Hit chance": 0.6,
            "stamina": 3,
            "Name": "test_enemy_name",
        }

    #Check if essential battle info is in printout
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_battle_stats_printout_in_battle(self, mock_output):
        print_battle_stats(self.test_character, self.test_enemy)
        self.assertIn("[IN BATTLE]", mock_output.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_battle_stats_printout_character_name(self, mock_output):
        print_battle_stats(self.test_character, self.test_enemy)
        self.assertIn("test_name", mock_output.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_battle_stats_printout_rank_title(self, mock_output):
        print_battle_stats(self.test_character, self.test_enemy)
        self.assertIn("Soldado", mock_output.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_battle_stats_printout_health(self, mock_output):
        print_battle_stats(self.test_character, self.test_enemy)
        self.assertIn("10", mock_output.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_battle_stats_printout_xp(self, mock_output):
        print_battle_stats(self.test_character, self.test_enemy)
        self.assertIn("0", mock_output.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_battle_stats_printout_enemy_name(self, mock_output):
        print_battle_stats(self.test_character, self.test_enemy)
        self.assertIn("test_enemy_name", mock_output.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_print_battle_stats_printout_enemy_hp(self, mock_output):
        print_battle_stats(self.test_character, self.test_enemy)
        self.assertIn("2", mock_output.getvalue())

