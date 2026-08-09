from lib.interface import * #importa todas as funções
from lib.arquivo import *
from colorama import init, Fore

init(autoreset=True)

if __name__ == '__main__':
    
    arq = 'cadastros.txt'
    if not arquivoExiste(arq):
        criarArquivo(arq)

    while True:
        resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema"])

        if resposta == 1:
            cabecalho('PESSOAS CADASTRADAS')
            sleep(1)
            lerArquivo(arq)
        elif resposta == 2:
            cabecalho('NOVO CADASTRO')
            nome = str(input('Nome: ')).capitalize()
            idade = leiaInt('Idade: ')
            cadastrar(arq, nome, idade)
            sleep(1)
        elif resposta == 3:
            cabecalho('ENCERRANDO SISTEMA...')
            break
        else:
            print(Fore.RED + "Erro: Digite uma opção valida!")