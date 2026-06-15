"""
Exercício 115 (A, B e C): Projeto do Mini-Sistema de Cadastro
Este é o projeto de encerramento do curso! Ele é dividido em três partes e simula um sistema profissional de terminal com armazenamento em ficheiro de texto (.txt).
-> Exercício 115a: Criando o Menu de Opções
    Crie um sistema com um menu principal estilizado no terminal, permitindo escolher entre:
    - Ver pessoas cadastradas.
    - Cadastrar nova pessoa.
    - Sair do sistema. A entrada do menu deve ser protegida por tratamento de erros.
-> Exercício 115b: Arquivando Dados
    Ao escolher a opção 1, o sistema deverá ler e mostrar o conteúdo de um ficheiro de texto chamado cursoemvideo.txt. Se o ficheiro não existir, o sistema deve criá-lo automaticamente.
-> Exercício 115c: Inserindo Dados no Arquivo
    Ao escolher a opção 2, o programa deve solicitar o nome e a idade da nova pessoa e gravá-los no ficheiro cursoemvideo.txt. Garanta que a idade seja validada pelo tratamento de erros.
"""

"""
Modulos principais da biblioteca Colorama
    Fore: Controla a cor do texto
    Back: Controla a cor de fundo do texto 
    Style: Controla a intensidade ou o estilo
OBS: Para que as cores funcionem corretamente no Windows, é necessário inicializar a biblioteca com init() logo no início do código -> Ex: init(autoreset = True)
"""

from colorama import init, Fore
from time import sleep

init(autoreset = True)

def linha(tam=40):
    """Gera uma linha divisória adaptável."""
    return('-'*tam)


def cabecalho(titulo):
    """Desenha um cabeçalho centralizado e estilizado."""
    print(linha())
    print(f'{titulo:^40}')
    print(linha())


def leiaInt(msg):
    """Lê um número inteiro com validação robusta contra erros."""
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(Fore.RED + 'ERRO: por favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print(Fore.RED + '\nUsuário preferiu não digitar esse número.')
            return 3 # Força a saída do sistema caso ele feche o input
        else:
            return num
        
def menu(lista):
    """Exibe o menu e retorna a opção validada do usuário."""
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f"{Fore.YELLOW}{c}{Fore.RESET} - {Fore.BLUE + item}")
        c +=1
    print(linha())
    opcao = leiaInt(f'{Fore.GREEN}Sua Opção: {Fore.RESET}')
    return opcao