from io import StringIO
from unittest import TestCase
from unittest.mock import mock_open, patch
from game import begin_narration
from io import StringIO

class Test(TestCase):
    #File Opening for correct storyline chapters
    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.input", return_value="n")
    def test_begin_narration_chapter_1_opens_start_file(self, _, mock_file):
        begin_narration(0)
        mock_file.assert_called_once_with("./storyline/start.txt", "r")

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.input", side_effect=["YOO","n"])
    def test_begin_narration_chapter_1_opens_start_file_invalid_then_valid_input(self, _, mock_file):
        begin_narration(0)
        mock_file.assert_called_once_with("./storyline/start.txt", "r")

    @patch("builtins.open", new_callable=mock_open)
    def test_begin_narration_chapter_1_opens_end_file(self, mock_file):
        begin_narration(1)
        mock_file.assert_called_once_with("./storyline/end.txt", "r")

    #Skip narration
    @patch("builtins.input", return_value="y")
    @patch("builtins.open", new_callable=mock_open)
    def test_begin_narration_valid_skip_input(self, mock_file, _):
        begin_narration(0)
        mock_file.assert_not_called()

    @patch("builtins.input", side_effect=["WOAH","y"])
    @patch("builtins.open", new_callable=mock_open)
    def test_begin_narration_skip_invalid_input_then_valid_skip_input(self, mock_file, _):
        begin_narration(0)
        mock_file.assert_not_called()

    #FileNotFoundError prints helpful user message
    @patch("builtins.input", return_value="n")
    @patch("builtins.open", side_effect=FileNotFoundError)
    @patch("sys.stdout", new_callable=StringIO)
    def test_begin_narration_missing_storyline_prints_helpful_user_message(self, mock_console_output, _,
                                                                           __):
            begin_narration(0)
            self.assertIn("Storyline file missing, please reinstall file.", mock_console_output.getvalue())













