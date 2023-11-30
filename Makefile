play:
	python3 qpr_quiz_game/main.py
clean:
	rm -rf .mypy_cache/ .pytest.cache/
	rm -rf qpr_quiz_game/.mypy_cache/ qpr_quiz_game/__pycache__ 
	rm -rf tests/__pycache__/
install:
	pip3 install -r requirements.txt
dev: install
	pip3 install -r dev-requirements.txt
test:
	pytest tests/test_*

help:
	@echo "Comandos disponíveis:"
	@echo -e "play\t\t: Jogar quiz"
	@echo -e "clean\t\t: Remover cache e outros arquivos e pastas desnecessários"
	@echo -e "install\t\t: Instalar dependências necessárias pelo pip para jogar"
	@echo -e "dev\t\t: Instalar dependência pelo pip para desenvolvedor"
	@echo -e "test\t\t: Realizes testes do código"