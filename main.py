from qpr_quiz_game.menu import mostrar_menu
from qpr_quiz_game.labels import TextLabel

if __name__ == "__main__":
    TextLabel.carregar_labels()
    mostrar_menu(TextLabel.labels)
