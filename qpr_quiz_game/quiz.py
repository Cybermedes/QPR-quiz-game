import random
import tomllib
import questionary
import qpr_quiz_game.menu as menu
import qpr_quiz_game.labels as ui_text

from pathlib import Path
from typing import Any
from string import ascii_lowercase
from rich.console import Console
from qpr_quiz_game.terminal import limpar_terminal, abortar_programa

console = Console()


def preparar_questoes(path: Path, num_questoes: int) -> list[dict[str, Any]]:
    """Lê um número fixo de questoes arquivo toml e as retorna de forma aleatória em uma lista"""

    lista_questoes: list[dict[str, Any]] = tomllib.loads(path.read_text())["questions"]
    num_questions = min(num_questoes, len(lista_questoes))

    return random.sample(lista_questoes, k=num_questions)


def fazer_pergunta(questao: dict[str, Any]) -> int:
    """Lança a pergunta no terminal e espera o input do jogador.
    Retorna 1 ponto se acertar e 0 se errar"""

    # Lê as perguntas, alternativas e resposta do repositório
    resposta_correta: str = questao["answer"]
    alternativas: list = [questao["answer"]] + questao["alternatives"]
    alternativas_ordenadas = random.sample(alternativas, k=len(alternativas))

    # Checa se a resposta é certa ou errada e dá pontuação
    resposta = pegar_resposta(questao["question"], alternativas_ordenadas)
    if resposta == resposta_correta:
        console.print(ui_text.QUIZ_RESPOSTA_CERTA[0].upper(), style="green")
        return 1
    else:
        console.print(
            ui_text.QUIZ_RESPOSTA_ERRADA[0].format(resposta_correta, resposta)
        )
        return 0


def pegar_resposta(pergunta, alternativas):
    """Imprime a pergunta e as alternativas e espera uma resposta do usuário. Caso
    a resposta seja inválida, faça a pergunta novamente"""

    print(f"{pergunta}")

    # Adiciona letras para cada alternativa e convert list para dict
    alternativas_letradas: dict[str, Any] = dict(zip(ascii_lowercase, alternativas))
    for letra, alternativa in alternativas_letradas.items():
        print(f"{letra}) {alternativa}")

    # Loop para validação da resposta do usuário
    while (
        alternativa_escolhida := input(ui_text.QUIZ_USER_INPUT[0])
    ) not in alternativas_letradas:
        console.print(
            ui_text.QUIZ_MENSAGEM_ERRO[0].format(", ".join(alternativas_letradas))
        )

    return alternativas_letradas[alternativa_escolhida]


@abortar_programa
def rodar_quiz() -> None:
    """Inicia o quiz após ler e preparar as perguntas"""

    # Pasta e aqruivo contendo as perguntas, respostas e alternativas
    questoes_path: Path = Path("quiz_database", "questions.toml")
    numero_perguntas: int = 5

    if questoes_path.exists():
        # Ler e selecionar as perguntas do arquivo com o banco de questões
        quiz: list[dict[str, Any]] = preparar_questoes(questoes_path, numero_perguntas)

        # pontuação
        num_corretas: int = 0

        # Main loop do quiz para mostrar perguntas, uma por vez
        for num, questao in enumerate(quiz, start=1):
            limpar_terminal()
            console.print(ui_text.QUIZ_QUESTAO[0].format(num).upper(), style="bold")
            num_corretas += fazer_pergunta(questao)
            questionary.press_any_key_to_continue(ui_text.QUIZ_INSTRUCAO[0]).ask()

        # Resultado final
        limpar_terminal()
        console.print(ui_text.QUIZ_RESULTADO_FINAL[0].format(num_corretas, len(quiz)))
        while True:
            jogar_novamente: str = input(ui_text.QUIZ_JOGAR_NOVAMENTE[0])
            if jogar_novamente.lower() == "s" or jogar_novamente.lower() == "y":
                rodar_quiz()
                break
            elif jogar_novamente.lower() == "n":
                menu.mostrar_menu()
                break
            else:
                console.print(ui_text.QUIZ_OPCAO_INVALIDA[0])

        # TODO customizar mais a mensagem de resultado final

    else:
        console.print(
            ui_text.QUIZ_SEM_DATABASE[0],
            style="red bold",
        )
