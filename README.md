# QPR-Quiz-game

```
  /$$$$$$  /$$$$$$$  /$$$$$$$         /$$$$$$            /$$          
 /$$__  $$| $$__  $$| $$__  $$       /$$__  $$          |__/          
| $$  \ $$| $$  \ $$| $$  \ $$      | $$  \ $$ /$$   /$$ /$$ /$$$$$$$$
| $$  | $$| $$$$$$$/| $$$$$$$/      | $$  | $$| $$  | $$| $$|____ /$$/
| $$  | $$| $$____/ | $$__  $$      | $$  | $$| $$  | $$| $$   /$$$$/ 
| $$/$$ $$| $$      | $$  \ $$      | $$/$$ $$| $$  | $$| $$  /$$__/  
|  $$$$$$/| $$      | $$  | $$      |  $$$$$$/|  $$$$$$/| $$ /$$$$$$$$
 \____ $$$|__/      |__/  |__/       \____ $$$ \______/ |__/|________/
      \__/                                \__/                        
```

Jogo de perguntas e respostas sobre programação no terminal

Requisitos:
- Terminal com UTF-8 (Powershell, Bash, Zsh, Mingw64)
- Python 3.11
- Pip
- Python venv
- Docker (caso não tenha Python instalado localmente)

## Como instalar

### Usando Python

Criar um ambiente virtual em Python:

```Bash
# Windows
python -m venv venv

# MacOS & Linux
python3 -m venv venv
```

Ativar o ambiente virtual:

```Bash
# Windows
C:\> venv\Scripts\activate.bat    # cmd.exe
PS C:\> venv\Scripts\Activate.ps1 # PowerShell

# MacOS & Linux
$ source venv/bin/activate      # bash/zsh
$ source venv/bin/activate.fish # fish
$ source venv/bin/activate.csh  # csh/tcsh
$ venv/bin/Activate.ps1         # PowerShell (POSIX)
```

Instalar dependências para poder jogar:

```bash
# Windows
pip install --upgrade -r requirements.txt

# MacOS & Linux
pip3 install --upgrade -r requirements.txt
```

Instalar dependências para desenvolvimento (opcional):

```bash
# Windows
pip install --upgrade -r dev-requirements.txt

# MacOS & Linux
pip3 install --upgrade -r dev-requirements.txt
```
### Usando Docker conteiner
