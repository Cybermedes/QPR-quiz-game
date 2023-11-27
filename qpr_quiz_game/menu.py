import questionary
import labels  # type: ignore

from rich.console import Console
from questionary import Style
from quiz import rodar_quiz  # type: ignore
from terminal import limpar_terminal  # type: ignore

console = Console()


def encerrar_programa() -> None:
    """Encerra programa e imprime mesagem de despedida"""
    limpar_terminal()
    console.print(labels.MENU_GOODBYE[0], style="green")


def saber_mais() -> None:
    """Imprime mais informações sobre o programa e link para o código fonte"""
    limpar_terminal()

    console.print(labels.MENU_MAIS[0])
    questionary.press_any_key_to_continue(labels.MENU_INSTRUCAO_2[0]).ask()
    mostrar_menu()


def mostrar_menu() -> None:
    """Imprime o menu principal no terminal"""

    limpar_terminal()
    titulo: str = str(labels.MENU_TITULO[0])
    console.print(titulo.upper(), style="cyan bold", justify="center")
    console.print(labels.MENU_VERSAO[0], style="italic", justify="left")

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
        message=labels.MENU_MENSAGEM[0],
        choices=labels.MENU_OPCOES[0],
        style=questionario_estilo,
        instruction=labels.MENU_INSTRUCAO_1[0],
    ).ask()

    match opcao:
        case "Jogar":
            rodar_quiz()
        case "Sobre":
            saber_mais()
        case "Sair":
            encerrar_programa()
        case _:
            print(f"Por favor seleciona umas das opções")
