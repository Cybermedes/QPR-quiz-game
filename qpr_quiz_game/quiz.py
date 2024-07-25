import random
import sys
import tomllib
import questionary
import qpr_quiz_game.menu as menu

from pathlib import Path
from typing import Any
from string import ascii_lowercase
from rich.console import Console
from qpr_quiz_game.labels import TextLabel
from qpr_quiz_game.terminal import limpar_terminal, abortar_programa

console = Console()


# noinspection SpellCheckingInspection
def preparar_questoes(path: Path, num_questoes: int) -> list[dict[str, Any]]:
    """Lê um número fixo de questões arquivo toml e as retorna de forma aleatória em uma lista"""

    lista_questoes: list[dict[str, Any]] = tomllib.loads(path.read_text())["questions"]
    num_questions = min(num_questoes, len(lista_questoes))

    return random.sample(lista_questoes, k=num_questions)


# noinspection SpellCheckingInspection
def fazer_pergunta(questao: dict[str, Any]) -> int:
    """Lança a pergunta no terminal e espera o input do jogador.
    Retorna 1 ponto se acertar e 0 se errar"""

    # Lê as perguntas, alternativas e resposta do repositório
    resposta_correta: str = questao["answer"]
    alternativas: list = [questao["answer"]] + questao["alternatives"]
    alternativas_ordenadas = random.sample(alternativas, k=len(alternativas))

    # Checa se a resposta é certa ou errada e dá pontuação
    resposta = pegar_resposta(questao["question"], alternativas_ordenadas)
    if resposta == resposta_correta:
        console.print(TextLabel.labels["quiz_right_answer"].upper(), style="green")
        return 1
    else:
        console.print(
            TextLabel.labels["quiz_wrong_answer"].format(resposta_correta, resposta)
        )
        return 0


def pegar_resposta(pergunta, alternativas):
    """Imprime a pergunta e as alternativas e espera uma resposta do usuário. Caso
    a resposta seja inválida, faça a pergunta novamente"""

    print(f"{pergunta}")

    # Adiciona letras para cada alternativa e convert list para dict
    alternativas_letradas: dict[str, Any] = dict(zip(ascii_lowercase, alternativas))
    for letra, alternativa in alternativas_letradas.items():
        print(f"{letra}) {alternativa}")

    # Loop para validação da resposta do usuário
    while (
            alternativa_escolhida := input(TextLabel.labels["quiz_user_input"])
    ) not in alternativas_letradas:
        console.print(
            TextLabel.labels["quiz_error_message"].format(", ".join(alternativas_letradas))
        )

    return alternativas_letradas[alternativa_escolhida]


# noinspection SpellCheckingInspection
@abortar_programa
def rodar_quiz() -> None:
    """Inicia o quiz após ler e preparar as perguntas"""

    # Pasta e arquivo contendo as perguntas, respostas e alternativas
    questoes_path: Path = Path("quiz_database", "questions.toml")
    numero_perguntas: int = 5

    try:
        # Ler e selecionar as perguntas do arquivo com o banco de questões
        quiz: list[dict[str, Any]] = preparar_questoes(questoes_path, numero_perguntas)

        # pontuação
        num_corretas: int = 0

        # Main loop do quiz para mostrar perguntas, uma por vez
        for num, questao in enumerate(quiz, start=1):
            limpar_terminal()
            console.print(TextLabel.labels["quiz_question"].format(num).upper(), style="bold")
            num_corretas += fazer_pergunta(questao)
            questionary.press_any_key_to_continue(TextLabel.labels["quiz_instruction"]).ask()

        # Resultado final
        limpar_terminal()
        console.print(TextLabel.labels["quiz_final_score"].format(num_corretas, len(quiz)))
        while True:
            jogar_novamente: str = input(TextLabel.labels["quiz_play_again"])
            if jogar_novamente.lower() == "s" or jogar_novamente.lower() == "y":
                rodar_quiz()
                break
            elif jogar_novamente.lower() == "n":
                menu.mostrar_menu()
                break
            else:
                console.print(TextLabel.labels["quiz_invalid_option"])

        # TODO customizar mais a mensagem de resultado final

    except FileNotFoundError:
        console.print(TextLabel.labels["quiz_no_database"], style="red bold")
        sys.exit(1)
