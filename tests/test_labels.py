import unittest

from pathlib import Path
from qpr_quiz_game.labels import TextLabel


class TestLabelClass(unittest.TestCase):

    def test_label_text_file_exists(self) -> None:
        """Test 'text_labels_pt.toml' file exists"""
        _lang_file: Path = Path("resources", "text_labels_pt.toml")
        self.assertTrue(_lang_file.exists())

    def test_file_is_loaded_and_read(self) -> None:
        """Test file is loaded and read"""
        TextLabel.carregar_labels()
        self.assertTrue(len(TextLabel.labels) >= 1)  # Check is not empty
        self.assertIsNotNone(TextLabel.labels)  # Check is not null
        self.assertIsInstance(TextLabel.labels, dict)  # Check if it is a dictionary

        # Check if key and values match
        expected: str = "Pressione qualquer tecla para continuar..."
        self.assertEqual(expected, TextLabel.labels["quiz_instruction"])
        expected: str = "\n✅ ⭐ Resposta Correta! ⭐\n"
        self.assertEqual(expected, TextLabel.labels["quiz_right_answer"])

    def test_all_values_are_correct_type(self) -> None:
        """Test the values of the dictionary are strings or list of strings"""
        TextLabel.carregar_labels()
        for key, value in TextLabel.labels.items():
            if key == "menu_options":
                self.assertIsInstance(value, list)
            else:
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
