"""Strings em português e inglês"""

# Strings Menu Principal
MENU_TITULO: tuple = (
    """
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
    """,
)
MENU_MAIS: tuple = (
    """\n\tO QPR é um quiz de perguntas e respostas sobre programação e TI, 
foi feito em Python 3.12 para Terminais como Bash, Zash ou Powershell.
Utilize as setas do teclado para navegar no menu principal e ENTER para confirmar. Para as
perguntas, digite a alternativa escolhida e aperte ENTER.
\tO código fonte é [italic]open source[/] e mais informações estão disponíveis no GitHub para acesso
através do link https://github.com/Cybermedes/QPR-quiz-game.\n""",
)
MENU_GOODBYE: tuple = ("👋 Tchau e até a próxima!",)
MENU_INSTRUCAO_1: tuple = ("(Use as setas e aperte ENTER)",)
MENU_INSTRUCAO_2: tuple = ("Pressione qualquer tecla para voltar ao menu principal...",)
MENU_VERSAO: tuple = ("Version: Alpha",)
MENU_OPCOES: tuple[list, list] = (["Jogar", "Sobre", "Sair"], [])
MENU_MENSAGEM: tuple = ("Selecione uma das opções abaixo:",)

# Strings do modulo quiz
QUIZ_RESPOSTA_CERTA: tuple = ("\n✅ ⭐ Resposta Correta! ⭐\n",)
QUIZ_RESPOSTA_ERRADA: tuple = (
    "\n❌ A resposta certa é [bold green]{}[/], não [bold red]{}[/].\n",
)
QUIZ_MENSAGEM_ERRO: tuple = ("🚫 Por favor responda com [cyan]{}[/]",)
QUIZ_QUESTAO: tuple = ("\nQuestão {}:",)
QUIZ_USER_INPUT: tuple = ("\nQual é a resposta? ",)
QUIZ_INSTRUCAO: tuple = ("Pressione qualquer tecla para continuar...",)
QUIZ_RESULTADO_FINAL: tuple = ("\nVocê acertou [bold underline]{}[/] perguntas "
                               + "de um total de [bold underline]{}[/] perguntas.",)
QUIZ_JOGAR_NOVAMENTE: tuple = ("\nJogar novamente [s/n]? ",)
QUIZ_OPCAO_INVALIDA: tuple = ("🚫 Por favor responda com [green]'s'[/] para sim ou [red]'n'[/] para não",)
QUIZ_SEM_DATABASE: tuple = ("⚠️ O arquivo \"questions.toml\" não foi encontrado ⚠️",)