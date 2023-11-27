import os


def limpar_terminal() -> int:
    """Limpar o terminal através de commando. cls para Windows ou clear para Unix"""
    return os.system("cls" if os.name in ("nt", "dos") else "clear")
