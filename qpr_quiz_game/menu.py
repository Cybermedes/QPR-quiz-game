import sys

import questionary

from rich.console import Console
from questionary import Style
from qpr_quiz_game.quiz import rodar_quiz
from qpr_quiz_game.terminal import limpar_terminal
from qpr_quiz_game.labels import TextLabel

console = Console()


def encerrar_programa() -> None:
    """Encerra programa e imprime mensagem de despedida"""
    limpar_terminal()
    console.print(TextLabel.labels["menu_goodbye"], style="green")
    sys.exit(0)


def saber_mais() -> None:
    """Imprime mais informações sobre o programa e link para o código-fonte"""
    limpar_terminal()

    console.print(TextLabel.labels["menu_info"])
    questionary.press_any_key_to_continue(TextLabel.labels["menu_instruction_two"]).ask()
    mostrar_menu()


# noinspection SpellCheckingInspection
def mostrar_menu() -> None:
    """Imprime o menu principal no terminal"""

    limpar_terminal()
    titulo: str = str(TextLabel.labels["menu_title"])
    console.print(titulo.upper(), style="cyan bold", justify="center")
    console.print(TextLabel.labels["menu_version"], style="italic", justify="left")

    # Estilo gráfico para as opções do menu principal
    questionario_estilo = Style(
        [
            ("qmark", "fg:#673ab7 bold"),
            ("highlighted", "fg:#e1bb0c bold"),
            ("pointer", "fg:#e1bb0c bold"),
        ]
    )

    # Opções para o usuário escolher
    opcao = questionary.select(
        message=TextLabel.labels["menu_message"],
        choices=TextLabel.labels["menu_options"],
        style=questionario_estilo,
        instruction=TextLabel.labels["menu_instruction_one"],
    ).ask()

    match opcao:
        case "Jogar":
            rodar_quiz()
        case "Sobre":
            saber_mais()
        case "Sair":
            encerrar_programa()
