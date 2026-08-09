# Este é o arquivo número 101
"""
Exercício 101: Funções para Votação

O que fazer: Crie um programa que tenha uma função chamada voto(), que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
Dica do Cleitin: Importe o módulo datetime dentro da própria função para economizar memória (escopo local de importação).
"""
from datetime import datetime

#idade = ano_atual - ano
def voto(ano):
    '''
    Função para saber a obrigatoriedade de voto a partir da idade de uma pessoa, informando o ano de nascimento.
    '''
    ano_atual = datetime.now().year
    idade = ano_atual - ano
    if idade < 16:
        return f"Com {idade} anos: NÃO PODE VOTAR!"
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO É OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO É OBRIGATORIO"


ano = int(input("Ano de Nascimento: "))
print(voto(ano))
