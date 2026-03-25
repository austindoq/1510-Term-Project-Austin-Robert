from unittest import TestCase
from simple_game import make_board
from unittest.mock import patch

class Test(TestCase):
    @patch('random.randint', return_value=0)
    def test_make_board_smallest_board(self, _):
        actual = make_board(1,1)
        expected = {
            (0,0) : "\033[32mYou are in an open field filled with long grass and small boulders.\033[0m"
        }
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=0)
    def test_make_board_typical_game_board(self, _):
        actual = make_board(5, 5)
        expected = {(0, 0): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (0, 1): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (0, 2): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (0, 3): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (0, 4): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (1, 0): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (1, 1): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (1, 2): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (1, 3): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (1, 4): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (2, 0): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (2, 1): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (2, 2): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (2, 3): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (2, 4): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (3, 0): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (3, 1): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (3, 2): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (3, 3): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (3, 4): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (4, 0): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (4, 1): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (4, 2): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (4, 3): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (4, 4): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m'}

        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=0)
    def test_make_board_rectangle(self, _):
        actual = make_board(1, 3)
        expected = {(0, 0): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (0, 1): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m',
                    (0, 2): '\x1b[32mYou are in an open field filled with long grass and small boulders.\x1b[0m'}

        self.assertEqual(expected, actual)

    def test_make_board_rows_alphabetical_input(self):
        with self.assertRaises(ValueError):
            make_board('a', 3)

    def test_make_board_columns_alphabetical_input(self):
        with self.assertRaises(ValueError):
            make_board(3, 'a')

    def test_make_board_rows_less_than_one(self):
        with self.assertRaises(ValueError):
            make_board(0, 1)

    def test_make_board_columns_less_than_one(self):
        with self.assertRaises(ValueError):
            make_board(1, 0)





