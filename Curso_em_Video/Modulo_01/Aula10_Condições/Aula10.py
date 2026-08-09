#Condições Simples e Compostas.
# Se = if + condição
# Senão = else + condição

#Exemplo 01
tempo = int(input('Quando tempo tem seu carro?: '))
#print('Carro novo' if tempo <= 3 else 'Carro velho') --> forma simplificada.
if tempo <= 3:
    print('Até que ta novo')
else:
    print('Carro veio podi')
print()
print('____________')

#Exemplo 02
nome = str(input('Qual seu nome?: ')).upper()
if 'CARLOS' in nome:
    print('Olá {}, telezé que nome bonito.'.format(nome))
else:
    print('Olá {}, que nome feio da poha'.format(nome))
print()
print('____________')

#Exemplo 03
n1 = float(input('Nota da primeira avaliação: '))
n2 = float(input('Nota da segunda avaliação: '))
m = (n1 + n2)/2
print('A sua média foi {}'.format(m))
if m >= 6.0:
    print('A sua média foi boa, PARABÉNS!')
else:
    print('Num trata de estudar!')
