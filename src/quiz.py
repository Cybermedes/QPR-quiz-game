import random
import tomllib
from pathlib import Path
from typing import Any
from string import ascii_lowercase


def preparar_questoes(path: Path, num_questoes: int) -> list[dict[str, Any]]:
    """Le as questoes arquivo toml e as retorna em uma lista"""
    with open(path, mode="rb") as toml_arquivo:
        questoes: dict[str, Any] = tomllib.load(toml_arquivo)
    num_questions = min(num_questoes, len(questoes))
    lista_questoes: list[dict[str, Any]] = questoes["questions"]

    return random.sample(lista_questoes, k=num_questions)


def fazer_pergunta(questao: dict[str, Any]) -> int:
    """Lança a pergunta no terminal e espera o input do jogador.
    Retorna 1 ponto se acertar e 0 se errar"""

    questao_principal: str = questao["question"]
    resposta_correta: str = questao["answer"]
    alternativas: list = [[questao["answer"]]] + questao["alternatives"]
    random.shuffle(alternativas)
    alternativas_numeradas = dict(zip(ascii_lowercase, alternativas))
    print(questao_principal)
    for letra, alternativa in alternativas_numeradas.items():
        print(f"{letra}) {alternativa}")

    resposta = input("Digite a resposta da alternativa correta: ")
    if resposta == resposta_correta:
        print("⭐ Resposta Correta! ⭐")
        return 1
    else:
        print(f"A resposta é {resposta_correta!r}, não {resposta!r}")
        return 0


def rodar_quiz() -> None:
    questoes_path: Path = Path().cwd().parent.joinpath("quiz_database", "questions.toml")
    numero_perguntas: int = 5
    
    if questoes_path.exists():
        # Ler e selecionar as perguntas do arquivo com o banco de questões
        questoes: list[dict[str, Any]] = preparar_questoes(questoes_path, numero_perguntas)

        # pontuação
        num_corretas: int = 0

        # Main loop do quiz para mostrar perguntas, uma por vez
        for questao in questoes:
            num_corretas += fazer_pergunta(questao)

        # Resultado final
        print(f"\nVocê acertou {num_corretas} perguntas")
        
    else:
        print(f"O arquivo \"questions.toml\" não foi encontrado")
