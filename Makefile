play:
    python3 qpr_quiz_game/main.py

clean:
    rm -rf qpr_quiz_game/.mypy_cache/

install:
    pip3 install -r requirements.txt

dev: install
    pip3 install -r dev-requirements.txt

test: