from rich.console import Console
from questionary import Style
import questionary


def mostrar_menu() -> None:
    titulo: str = """
    *********************
    🎲🏆🤓⭐ QPR ⭐🎲🏆🤓
    *********************
    
    Quiz de perguntas e respostas no Terminal sobre programação
    """

    console = Console()
    console.print(titulo, style="cyan bold")

    questionario_estilo = Style([
        ('qmark', 'fg:#673ab7 bold'),
        ('highlighted', 'fg:#e1bb0c bold'),
        ('pointer', 'fg:#e1bb0c bold'),
    ])
    questionary.select(
        message="Selecione uma das opções abaixo:",
        choices=[
            "Jogar", "Sobre", "Sair"
        ],
        style=questionario_estilo,
        instruction="(Use as setas e aperte ENTER)"
    ).ask()
