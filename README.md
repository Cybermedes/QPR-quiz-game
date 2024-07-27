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

Um jogo de perguntas e respostas sobre programação no terminal feito em Python.

## Características

- Menu interativo: semelhante aos main menu de video-games, onde o cursor se movimenta com as setas do teclado
- Colorido: textos em cores e estilos diferentes e emojis
- Autoclean: a cada página o programa automaticamente limpa o terminal
- Docker: como foi projetado para rodar no terminal, não possui gui e pode rodar em docker contêineres ou 
máquinas virtuais, seja física ou cloud (desde que tenha acesso ao terminal e Python instalado)

## Como funciona

Ao iniciar o programa, o terminal do usuário será limpo e um menu principal será impresso com três
opções para escolher: 

- `Jogar`: para começar a jogar
- `Sobre`: para ler um texto com informações básicas sobre o programa
- `Sair`: para sair e encerrar o programa

Ao clicar em `Jogar`, o programa irá ler um arquivo `toml` ([o que é um arquivo toml](https://toml.io/en/)) chamado
`quiz_database/questions.toml`. Basicamente, esse arquivo contém uma lista de perguntas, cada uma com as suas
alternativas e uma resposta correta. O programa irá selecionar aleatoriamente 5 dessas perguntas, embaralhar a
ordem das alternativas (para evitar padrões de repetição), e ordenar todas as alternativas em 'a', 'b', 'c', 'd', ...
E assim em diante.

Para responder, basta o usuário digitar a letra correspondente a alternativa que ele julgue ser a correta. O input não
faz diferença ser maiúsculo ou minúsculo, se o input for inválido (um número, por exemplo) ou que não coincida com
nenhuma alternativa (letra 'x' ou 'z', por exemplo), o programa irá perguntar novamente pela resposta do usuário.

Caso o input do usuário esteja correto, uma mensagem irá aparecer e pedir para clicar e continuar para a pŕoxima;
caso o input esteja errado, uma mensagem com a reposta certa em verde e a alternativa escolhida em vermelho irá aparecer.

Após o término das 5 perguntas, o usuário poderá saber quantas perguntas acertou, e se ele quer jogar novamente ou não.
Se a resposta for negativa, ele será redirecionado ao menu principal, se positiva, ele irá jogar novamente. Desta vez
o programa irá repetir novamente os passos de ler as questões e as embaralhar as alternativas. Com isso, reduzindo os
casos de repetição na ordem das questões e alternativas.

## Requisitos

- Terminal com UTF-8 (Powershell, Bash, Zsh, Mingw64)
- Python 3.11
- Pip
- Python venv
- Docker (caso não tenha Python instalado localmente)

## Como instalar

### Usando Python

Caso você tenha Python instalado no seu computador e deseja rodar localmente, basta dar um git clone nesse
repositório ou fazer o download dos arquivos. É recomendado criar um ambiente virtual em Python para
instalar as dependências necessárias para o programa poder funcionar. Comando para criar um ambiente virtual:

```Bash
# Windows
python -m venv venv

# MacOS & Linux
python3 -m venv venv
```

Ativar o ambiente virtual:

```bash
# Windows
C:\> venv\Scripts\activate.bat    # cmd.exe
PS C:\> venv\Scripts\Activate.ps1 # PowerShell

# MacOS & Linux
$ source venv/bin/activate      # bash/zsh
$ source venv/bin/activate.fish # fish
$ source venv/bin/activate.csh  # csh/tcsh
$ venv/bin/Activate.ps1         # PowerShell (POSIX)
```

Instalar dependências necessárias para poder jogar:

```bash
# Windows
pip install --upgrade -r requirements.txt

# MacOS & Linux
pip3 install --upgrade -r requirements.txt
```

Algumas ferramentas sugeridas para instalar dependências para desenvolvimento (opcional), para aqueles que 
desejam modificar o código ou criar a pŕopria versão:

```bash
# Windows
pip install --upgrade -r dev-requirements.txt

# MacOS & Linux
pip3 install --upgrade -r dev-requirements.txt
```
### Usando Docker contêiner

Caso você não tenha Python instalado no seu computador, uma alternativa seria você utilizar um
contêiner [Docker](https://www.docker.com/). Este repositório já contém um `Dockerfile`, para rodar
o game, basta digitar os comandos abaixo para criar uma imagem primeiro e depois executar um contêiner.

```bash
# build docker image
docker build -t quiz-game .
# run the docker container
docker run -it --name my-quiz-game quiz-game
```
