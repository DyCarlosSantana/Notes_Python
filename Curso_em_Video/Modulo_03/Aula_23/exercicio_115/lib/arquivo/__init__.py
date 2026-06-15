from lib.interface import *
from colorama import init, Fore

init(autoreset=True)

def arquivoExiste(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt') # rt (read text) - usando para leitura de arquivo
        a.close() # Fecha o arquivo
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nomeArquico):
    try:
        a = open(nomeArquico, 'wt+') # wt (write texte) - usado para escrever/criar um arquivo. O sinal (+) cria o arquivo se ele não existir
        a.close()
    except:
        print(Fore.RED + f'Houve um erros na criação do arquivo {nomeArquico}')
    else:
        print(Fore.GREEN + f'Arquivo {nomeArquico} criado com sucesso')


def lerArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print(Fore.RED + f'Erro ao ler o arquivo {nomeArquivo}')
    else:
        for linha in a:
            dado = linha.split(',') # Separa os dados usando split()
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos') # Realiza a leitura do arquivo
    finally:
        a.close


def cadastrar(nomeArquivo, nomePessoa, idade):
    try:
        a = open(nomeArquivo, 'at') # at ()
    except:
        print(Fore.RED + 'Erro na LEITURA do arquivo')
    else:
        try:
            a.write(f'{nomePessoa},{idade}\n')
            print(Fore.GREEN + f'Novos Dados cadastrados com sucesso')
        except:
            print(Fore.RED + 'Erro ao realizar novo Cadastro')
    finally:
        a.close