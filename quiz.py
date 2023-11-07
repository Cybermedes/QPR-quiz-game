"""Script para preparar as perguntas e respostas"""
def rodar_quiz() -> None:

    # Ler e selecionar as perguntas do arquivo com o banco de questões
    questoes = preparar_questoes()

    # pontuação
    num_corretas: int = 0

    # Main loop do quiz para mostrar perguntas, uma por vez
    for questao in questoes:
        num_corretas += fazer_pergunta(questao)

    # Resultado final
    print(f"\nVocê acertou {num_corretas} perguntas")
