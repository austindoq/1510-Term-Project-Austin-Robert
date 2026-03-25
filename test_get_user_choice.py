from unittest import TestCase
from game import get_user_choice
from unittest.mock import patch
import io

class Test(TestCase):
    @patch('builtins.input', side_effect='2')
    def test_get_user_choice_valid_selection_choice(self, _):
        expected = 2
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    #Function loops until valid choice is made
    @patch('builtins.input', side_effect=['5', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_invalid_selection_choice_then_valid(self, mock_output, _):
        get_user_choice()
        expected = ("You must choose a number from the listed options, you chose '5' which is not included in the list"
                    " of options. Please choose again.")
        self.assertIn(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect='word')
    def test_get_user_choice_word_input(self, _):
        self.assertRaises(ValueError)
