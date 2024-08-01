import random
import tomllib
from pathlib import Path
from string import ascii_lowercase
from typing import Any

from rich.console import Console

from qpr_quiz_game.labels import TextLabel

console = Console()


# noinspection SpellCheckingInspection
def preparar_questoes(path: Path, num_questoes: int) -> list[dict[str, Any]]:
    """Lê um número fixo de questões arquivo toml e as retorna de forma aleatória em uma lista"""

    lista_questoes: list[dict[str, Any]] = tomllib.loads(path.read_text())["questions"]
    num_questions = min(num_questoes, len(lista_questoes))

    return random.sample(lista_questoes, k=num_questions)


# noinspection SpellCheckingInspection
def fazer_pergunta(questao: dict[str, Any]) -> int:
    """Lança a pergunta no terminal e espera o input do jogador.
    Retorna 1 ponto se acertar e 0 se errar"""

    # Lê as perguntas, alternativas e resposta do repositório
    resposta_correta: str = questao["answer"]
    alternativas: list[Any] = [questao["answer"]] + questao["alternatives"]
    alternativas_ordenadas: list[Any] = random.sample(alternativas, k=len(alternativas))

    # Checa se a resposta é certa ou errada e dá pontuação
    resposta: Any = pegar_resposta_do_jogador(questao["question"], alternativas_ordenadas)
    if resposta == resposta_correta:
        console.print(TextLabel.labels["quiz_right_answer"].upper(), style="green")
        return 1
    else:
        console.print(
            TextLabel.labels["quiz_wrong_answer"].format(resposta_correta, resposta)
        )
        return 0


def pegar_resposta_do_jogador(pergunta: str, alternativas: list) -> Any:
    """Imprime a pergunta e as alternativas e espera uma resposta do usuário. Caso
    a resposta seja inválida, faça a pergunta novamente"""

    print(f"{pergunta}")

    alternativas_letradas = ordenar_alternativas(alternativas)

    # Loop para validação da resposta do usuário
    while (
            alternativa_escolhida := input(TextLabel.labels["quiz_user_input"])
    ) not in alternativas_letradas:
        console.print(
            TextLabel.labels["quiz_error_message"].format(", ".join(alternativas_letradas))
        )

    return alternativas_letradas[alternativa_escolhida]


def ordenar_alternativas(alternativas: list) -> dict[str, Any]:
    """Adiciona letras para cada alternativa e convert list para dict"""

    alternativas_letradas: dict[str, Any] = dict(zip(ascii_lowercase, alternativas))
    for letra, alternativa in alternativas_letradas.items():
        print(f"{letra}) {alternativa}")
    return alternativas_letradas
