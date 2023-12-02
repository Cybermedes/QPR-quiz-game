import sys
import subprocess
from rich.console import Console
import labels as ui_text  # type: ignore


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
            cons.print(ui_text.QUIZ_MENSAGEM_ABORTADA[0])

    return abortar
