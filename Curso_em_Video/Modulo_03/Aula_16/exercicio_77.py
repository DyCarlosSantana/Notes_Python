'''
    77 - Crie um programa que tenha uma tupla com varias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra quais são as suas vogais.
'''

palavras = (
    "zebra", "teto", "plano", "disco", "pasta", 
    "salto", "grito", "pedra", "casco", "lente", 
    "bloco", "fundo", "porto", "trilho", "sorte"
)

print('-'*40)
print(f'{"VOGAIS DE CADA PALAVRA":^40}')
print('-'*40)
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=', ')