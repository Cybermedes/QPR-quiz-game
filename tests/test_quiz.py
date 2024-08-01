import unittest
from pathlib import Path
from typing import Any

from qpr_quiz_game.quiz import preparar_questoes, ordenar_alternativas


class TestQuizClass(unittest.TestCase):
    # language=TOML
    __template: str = """[[questions]]
question = "Which version of Python is the first with TOML support built in"
answer = "3.11"
alternatives = ["3.9", "3.10", "3.12"]

[[questions]]
question = "What's the name of the list-like data structure in TOML?"
answer = "Array"
alternatives = ["List", "Sequence", "Set"]

[[questions]]
question = "How can you run a Python script named quiz.py?"
answer = "python quiz.py"
alternatives = ["python quiz", "./quiz.py", "python -m quiz"]

[[questions]]
question = "What's a PEP"
answer = "A Python Enhancement Proposal"
alternatives = ["A Pretty Exciting Policy", "A Preciously Evolved Python", "A Potentially Epic Prize"]
    
[[questions]]
question = "When was the first public version of Python released?"
answer = "February 1991"
alternatives = ["January 1994", "October 2000", "December 2008"]
"""

    @classmethod
    def setUpClass(cls) -> None:
        with open("temp_questions.toml", "w") as file:
            file.write(TestQuizClass.__template)

    def test_given_file_return_list_of_questions(self) -> None:
        """Test method return list of questions"""
        tmp_file_path: Path = Path("temp_questions.toml")
        actual: list[dict[str, Any]] = preparar_questoes(tmp_file_path, 4)
        self.assertEqual(len(actual), 4)  # Assert list contains 2 dicts
        self.assertTrue(len(actual) > 0)  # Assert list is not empty
        self.assertIsNotNone(actual)  # Assert list is not null
        self.assertTrue(len(actual[2]) >= 2)  # Assert alternative is greater or equal than 2
        # Assert list has unique
        for i in range(2):
            self.assertNotEqual(actual[i], actual[i + 1])

    def test_alternatives_have_letters(self) -> None:
        sample_list: list[str] = ["Java", "Python", "Go", "C"]
        actual: dict[str, Any] = ordenar_alternativas(sample_list)
        expected: dict[str, str] = {"a": "Java", "b": "Python", "c": "Go", "d": "C"}
        self.assertEqual(actual, expected)

    @classmethod
    def tearDownClass(cls) -> None:
        tmp_file: Path = Path("temp_questions.toml")
        tmp_file.unlink(missing_ok=False)


if __name__ == '__main__':
    unittest.main()
