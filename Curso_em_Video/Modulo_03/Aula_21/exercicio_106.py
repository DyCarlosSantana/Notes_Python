# Este é o arquivo número 106
"""
Exercício 106: Sistema Interativo de Ajuda

O que fazer: Faça um mini-sistema que utilize o Interactive Help do Python. O utilizador vai digitar o comando e o manual vai aparecer. Quando o utilizador digitar a palavra 'FIM', o programa se encerrará. Use cores para personalizar os menus e os fundos das respostas.
"""

def explica(msg):
    """
    Utiliza o Interactive Help para retornar a documentação de um função de forma simples e direta.
    Digite o nome da função ou biblioteca que deseja buscar a documentação.
    """
    while True:
        nome = str(input(msg)).strip().lower()
        if nome == 'fim':
            print('Finalizando programa!')
            break
        else:
            print('--+--'*10)
            help(nome)
            print('--+--'*10)


print('Para finalizar digite "FIM"')
pesquisa = explica('Função ou Biblioteca >> ')
