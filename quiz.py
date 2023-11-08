import random
import tomllib
from pathlib import Path
"""Script para preparar as perguntas e respostas"""


def preparar_questoes(path: Path, num_questoes: int = 5) -> list[str]:

    # Le as questões do arquivo toml
    with open(path, mode="rb") as toml_arquivo:
        questoes = tomllib.load(toml_arquivo)
    num_questions = min(num_questoes, len(questoes))

    # Retorna as questões em uma lista aleatória
    return random.sample(questoes, k=num_questions)


def fazer_pergunta(questao):
    pass


def rodar_quiz() -> None:
    questoes_path: Path = Path("questions.toml")

    # Ler e selecionar as perguntas do arquivo com o banco de questões
    questoes: list[str] = preparar_questoes(questoes_path)

    # pontuação
    num_corretas: int = 0

    # Main loop do quiz para mostrar perguntas, uma por vez
    for questao in questoes:
        num_corretas += fazer_pergunta(questao)

    # Resultado final
    print(f"\nVocê acertou {num_corretas} perguntas")
