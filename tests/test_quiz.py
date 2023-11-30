from pathlib import Path


def test_quiz_path():
    path_esperado: str = "quiz_database/questions.toml"
    path_atual: Path = Path("quiz_database", "questions.toml")

    assert path_atual.exists()
    assert path_atual.as_posix().__eq__(path_esperado)
