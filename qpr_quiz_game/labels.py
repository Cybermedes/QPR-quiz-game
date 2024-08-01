import sys
import tomllib
from pathlib import Path


class TextLabel:
    """Strings em português e inglês"""

    labels: dict[str, str] = dict()
    _lang_file: Path = Path("resources", "text_labels_pt.toml")

    @classmethod
    def carregar_labels(cls) -> None:
        try:
            with open(TextLabel._lang_file, "r") as file:
                TextLabel.labels = tomllib.loads(file.read())
        except FileNotFoundError as err:
            print(f"{type(err).__name__}: Arquivo 'resources/text_labels_pt.toml' não encontrado.")
            sys.exit(1)
