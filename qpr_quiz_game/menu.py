import questionary
import qpr_quiz_game.labels as ui_text

from rich.console import Console
from questionary import Style
from qpr_quiz_game.quiz import rodar_quiz
from qpr_quiz_game.terminal import limpar_terminal

console = Console()


def encerrar_programa() -> None:
    """Encerra programa e imprime mesagem de despedida"""
    limpar_terminal()
    console.print(ui_text.MENU_GOODBYE[0], style="green")


def saber_mais() -> None:
    """Imprime mais informações sobre o programa e link para o código fonte"""
    limpar_terminal()

    console.print(ui_text.MENU_MAIS[0])
    questionary.press_any_key_to_continue(ui_text.MENU_INSTRUCAO_2[0]).ask()
    mostrar_menu()


def mostrar_menu() -> None:
    """Imprime o menu principal no terminal"""

    limpar_terminal()
    titulo: str = str(ui_text.MENU_TITULO[0])
    console.print(titulo.upper(), style="cyan bold", justify="center")
    console.print(ui_text.MENU_VERSAO[0], style="italic", justify="left")

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
        message=ui_text.MENU_MENSAGEM[0],
        choices=ui_text.MENU_OPCOES[0],
        style=questionario_estilo,
        instruction=ui_text.MENU_INSTRUCAO_1[0],
    ).ask()

    match opcao:
        case "Jogar":
            rodar_quiz()
        case "Sobre":
            saber_mais()
        case "Sair":
            encerrar_programa()
