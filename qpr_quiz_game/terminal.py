import sys
import subprocess
from rich.console import Console
from qpr_quiz_game.labels import TextLabel


def limpar_terminal() -> None:
    """Limpar o terminal através de commando dependendo do S.O."""
    sistema_operacional: str = sys.platform

    # win32 para sistemas Windows
    # darwin para MacOS e cygwin para emuladores Linux no windows, como MINGW64
    if sistema_operacional == "win32":
        subprocess.run("cls", shell=True)
    elif (
        sistema_operacional == "darwin"
        or sistema_operacional == "linux"
        or sistema_operacional == "cygwin"
    ):
        subprocess.run("clear", shell=True)


def abortar_programa(func):
    """Decorator para fazer tratamento de exceção quando forçar parada do programa"""

    cons = Console(style="red bold")

    def abortar():
        try:
            func()
        except KeyboardInterrupt:
            cons.print(TextLabel.labels["quiz_aborted_message"])
            sys.exit(1)
    return abortar
