#Crie um programa que leia uma frase qualque e diga se ela é um polindromo, desconsidereando os espaços.
frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()#divisão das palavras
junto = ''.join(palavras)#tira os espacos ou os substitui as palavras

#Inverte a str.
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

#Verifica se é ou não um palíndromo.
if inverso == junto:
    print('Temos um Palíndromo!')
    print('Você digitou a frase: {}, e invertida ela fica: {}.'.format(frase, inverso))
else:
    print('A frase digitada não é um Palíndromo')
    print('Você digitou a frase: {}, e invertida ela fica: {}.'.format(frase, inverso))

#pode ser feito de forma mais simplificada sem o conceito de laço (for)
print('_'*30)
print('Segundo Exemplo')
print('')

frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()#divisão das palavras
junto = ''.join(palavras)#tira os espacos ou os substitui as palavras
inverso = junto[:: -1] #Inverte a str.

#Verifica se é ou não um palíndromo.
if inverso == junto:
    print('Temos um Palíndromo!')
    print('Você digitou a frase: {}, e invertida ela fica: {}.'.format(frase, inverso))
else:
    print('A frase digitada não é um Palíndromo')
    print('Você digitou a frase: {}, e invertida ela fica: {}.'.format(frase, inverso))
