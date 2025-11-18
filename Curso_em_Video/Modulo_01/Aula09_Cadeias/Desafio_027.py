#Verificação do nome completo de uma pessoa, e mostre o primeiro, segundo e ultimo sobrenome nome dessa pessoa.

nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(n[0]))
print('E seu segundo nome é {}'.format(n[1]))
print('E seu ultimo sobrenome é {}'.format(n[len(n)-1]))