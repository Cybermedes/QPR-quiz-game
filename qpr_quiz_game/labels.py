import sys
import tomllib
from pathlib import Path


class TextLabel:
    """Strings em português e inglês"""

    labels: dict[str, str] = dict()

    @classmethod
    def carregar_labels(cls) -> None:
        lang_file: Path = Path("resources", "text_labels_pt.toml")
        try:
            with open(lang_file, "r") as file:
                TextLabel.labels = tomllib.loads(file.read())
        except FileNotFoundError:
            print(f"Arquivo '{lang_file}' não encontrado, não foi possível iniciar o programa")
            print(f"File '{lang_file}' not found, could not start the program")
            sys.exit(1)
