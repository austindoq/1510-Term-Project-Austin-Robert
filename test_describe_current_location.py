from unittest import TestCase
from game import describe_current_location
from unittest.mock import patch
import io


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_is_on_board(self, mock_output):
        mock_board = {
            (0,0): 'You are in an open field filled with long grass and small boulders.',
            (0,1): 'You enter a sparsely wooded area, the trees are thin and bushes surround the trail.',
            (0,2): 'You are in a arid plane, little vegetation grows here and the wind blows strong.',
            (0,4): 'You are under a thick forest canopy, light struggles to reach the forest floor.'
        }
        mock_character = {"X-coordinate": 0,"Y-coordinate": 0,"Current HP": 5,"Name": "Doris"}
        expected = 'You are in an open field filled with long grass and small boulders.'
        describe_current_location(mock_board, mock_character)
        self.assertEqual(mock_output.getvalue().strip('\n'), expected)

    def test_describe_current_location_not_on_board(self):
        mock_board = {
            (0, 0): 'You are in an open field filled with long grass and small boulders.',
            (0, 1): 'You enter a sparsely wooded area, the trees are thin and bushes surround the trail.',
            (0, 2): 'You are in a arid plane, little vegetation grows here and the wind blows strong.',
            (0, 4): 'You are under a thick forest canopy, light struggles to reach the forest floor.'
        }
        mock_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Name": "Doris"}
        describe_current_location(mock_board, mock_character)
        self.assertRaises(KeyError)