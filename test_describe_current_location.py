from unittest import TestCase
from game import describe_current_location
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
        self.test_board = {
            (0, 0): "A dark forest",
            (0, 1): "A open field",
            (0, 2): "A rocky path",
            (1, 0): "A river bank",
            (1, 1): "A dusty cave",
            (1, 2): "A snowy peak",
            (2, 0): "A open field",
            (2, 1): "A dark forest",
            (2, 2): "A river bank",
        }
        self.rows = 3
        self.columns = 3

    @patch("sys.stdout", new_callable=StringIO)
    def test_describe_current_location_correctly_matched_to_tuple_location_description(self, mock_output):
        describe_current_location(self.test_board, self.test_character, self.rows, self.columns)
        self.assertIn("A dark forest", mock_output.getvalue())