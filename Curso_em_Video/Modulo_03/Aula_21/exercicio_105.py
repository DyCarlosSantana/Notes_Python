# Este é o arquivo número 105
"""
Exercício 105: Analisando e Gerando Dicionários
O que fazer: Faça um programa que tenha uma função notas(), que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
Quantidade de notas.
A maior nota.
A menor nota.
A média da turma.
A situação (opcional - Excelente/Boa/Razoável/Ruim).
Adicione também as Docstrings da função para que outros programadores saibam como usá-la.
"""

def notas(*nota, sit=False):
    '''
        A função nota() recebe as notas e analisa a maior e menor dentre as notas fornecidas. Assim como calcula a media de todas elas, incluindo a quantidade de notas fornecidas. Retornando como resultado um dicionario.
        Exemplo de resultado:
        {'Total': qtd_total, 'Maior': maior, 'Menor': menor, 'Média': media}
    '''
    
    maior = max(nota)
    menor = min(nota)
    media = sum(nota) / len(nota)
    qtd_total = len(nota)
    resultado = {'Total': qtd_total, 'Maior': maior, 'Menor': menor, 'Média': media}
    if sit:
        if media >= 7:
            resultado['Situação'] = 'Boa'
        elif media >= 5:
            resultado['Situação'] = 'Roazoavel'
        else:
            resultado['Situação'] = 'Ruim'
    return resultado 

resp = notas(5, 6, 8, sit=True)
print(resp)
