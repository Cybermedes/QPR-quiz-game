import sys
import subprocess


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
