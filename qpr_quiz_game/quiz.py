import os
import random
import tomllib
import questionary
from pathlib import Path
from typing import Any
from string import ascii_lowercase


def limpar_terminal() -> int:
    """Limpar o terminal através de commando. cls para Windows ou clear para Unix"""
    return os.system("cls" if os.name in ("nt", "dos") else "clear")


def preparar_questoes(path: Path, num_questoes: int) -> list[dict[str, Any]]:
    """Le as questoes arquivo toml e as retorna em uma lista"""

    lista_questoes: list[dict[str, Any]] = tomllib.loads(path.read_text())["questions"]
    num_questions = min(num_questoes, len(lista_questoes))

    return random.sample(lista_questoes, k=num_questions)


def fazer_pergunta(questao: dict[str, Any]) -> int:
    """Lança a pergunta no terminal e espera o input do jogador.
    Retorna 1 ponto se acertar e 0 se errar"""

    resposta_correta: str = questao["answer"]
    alternativas: list = [questao["answer"]] + questao["alternatives"]
    alternativas_ordenadas = random.sample(alternativas, k=len(alternativas))

    resposta = pegar_resposta(questao["question"], alternativas_ordenadas)
    if resposta == resposta_correta:
        print("⭐ Resposta Correta! ⭐")
        return 1
    else:
        print(f"A resposta é {resposta_correta!r}, não {resposta!r}")
        return 0


def pegar_resposta(pergunta, alternativas):
    print(f"{pergunta}")
    alternativas_letradas = dict(zip(ascii_lowercase, alternativas))
    for letra, alternativa in alternativas_letradas.items():
        print(f"{letra}) {alternativa}")

    while (
            alternativa_escolhida := input("\nQual é a resposta? ")
    ) not in alternativas_letradas:
        print(f"Por favor responda com {', '.join(alternativas_letradas)}")

    return alternativas_letradas[alternativa_escolhida]


def rodar_quiz() -> None:
    questoes_path: Path = (
        Path("quiz_database", "questions.toml")
    )
    numero_perguntas: int = 5

    if questoes_path.exists():
        # Ler e selecionar as perguntas do arquivo com o banco de questões
        quiz: list[dict[str, Any]] = preparar_questoes(questoes_path, numero_perguntas)

        # pontuação
        num_corretas: int = 0

        # Main loop do quiz para mostrar perguntas, uma por vez
        for num, questao in enumerate(quiz, start=1):
            limpar_terminal()
            print(f"\nQuestão {num}:")
            num_corretas += fazer_pergunta(questao)
            questionary.press_any_key_to_continue(
                "Pressione qualquer tecla para continuar..."
            ).ask()

        # Resultado final
        print(
            f"\nVocê acertou {num_corretas} perguntas de um total de {len(quiz)} perguntas."
        )
    else:
        print(f'O arquivo "questions.toml" não foi encontrado')
