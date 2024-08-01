import sys
from pathlib import Path
from typing import Any

import questionary
from rich.console import Console

import qpr_quiz_game.menu as menu
from qpr_quiz_game.labels import TextLabel
from qpr_quiz_game.quiz import preparar_questoes, fazer_pergunta
from qpr_quiz_game.terminal import limpar_terminal, abortar_programa

console = Console()


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
            print("\033[38;5;98;4;1m" + TextLabel.labels["quiz_question"].format(num).upper() + "\033[0m")
            # console.print(TextLabel.labels["quiz_question"].format(num).upper(), style="bold underline")
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
                menu.mostrar_menu(TextLabel.labels)
                break
            else:
                console.print(TextLabel.labels["quiz_invalid_option"])

        # TODO customizar mais a mensagem de resultado final

    except FileNotFoundError:
        console.print(TextLabel.labels["quiz_no_database"], style="red bold")
        sys.exit(1)
