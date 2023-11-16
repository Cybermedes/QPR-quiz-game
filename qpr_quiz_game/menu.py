from rich.console import Console
from questionary import Style
from quiz import rodar_quiz, limpar_terminal
import questionary

console = Console()


def saber_mais() -> None:
    # TODO adicionar string contendo informações sobre a aplicação
    pass


def mostrar_menu() -> None:
    limpar_terminal()
    titulo: str = """
    ##########################################################
    **********************************************************
     ██████╗ ██╗   ██╗██╗███████╗     ██████╗ ██████╗ ██████╗ 
    ██╔═══██╗██║   ██║██║╚══███╔╝    ██╔═══██╗██╔══██╗██╔══██╗
    ██║   ██║██║   ██║██║  ███╔╝     ██║   ██║██████╔╝██████╔╝
    ██║▄▄ ██║██║   ██║██║ ███╔╝      ██║▄▄ ██║██╔═══╝ ██╔══██╗
    ╚██████╔╝╚██████╔╝██║███████╗    ╚██████╔╝██║     ██║  ██║
    ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝     ╚══▀▀═╝ ╚═╝     ╚═╝  ╚═╝
    
    **********************************************************
    ##########################################################
    🎲🏆🤓⭐ QPR ⭐🎲🏆🤓
    **********************************************************
    
    🎮 Quiz de perguntas e respostas no Terminal sobre programação 🎮
    """

    console.print(titulo.upper(), style="cyan bold", justify="center")

    questionario_estilo = Style(
        [
            ("qmark", "fg:#673ab7 bold"),
            ("highlighted", "fg:#e1bb0c bold"),
            ("pointer", "fg:#e1bb0c bold"),
        ]
    )
    opcao = questionary.select(
        message="Selecione uma das opções abaixo:",
        choices=["Jogar", "Sobre", "Sair"],
        style=questionario_estilo,
        instruction="(Use as setas e aperte ENTER)",
    ).ask()

    match opcao:
        case "Jogar":
            rodar_quiz()
        case "Sobre":
            saber_mais()
        case "Sair":
            # TODO adicionar mensagem ao sair da aplicação
            pass
        case _:
            print(f"Por favor seleciona umas das opções")
