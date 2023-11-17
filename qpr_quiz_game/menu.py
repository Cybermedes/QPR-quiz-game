from rich.console import Console
from questionary import Style
import questionary
from quiz import rodar_quiz, limpar_terminal    # type: ignore

console = Console()


def encerrar_programa() -> None:
    limpar_terminal()
    console.print("👋 Tchau e até a próxima!", style="green")


def saber_mais() -> None:
    limpar_terminal()

    console.print("""\n\tO QPR é um quiz de perguntas e respostas sobre programação e TI, 
foi feito em Python 3.12 para Terminais como Bash, Zash ou Powershell.
Utilize as setas do teclado para navegar no menu principal e ENTER para confirmar. Para as
perguntas, digite a alternativa escolhida e aperte ENTER.
\tO código fonte é [italic]open source[/] e mais informações estão disponíveis no GitHub para acesso
através do link https://github.com/Cybermedes/QPR-quiz-game.\n""")
    questionary.press_any_key_to_continue("Pressione qualquer tecla para voltar ao menu principal...").ask()
    mostrar_menu()


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
    console.print("Version: Alpha", style="italic", justify="left")

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
            encerrar_programa()
        case _:
            print(f"Por favor seleciona umas das opções")
