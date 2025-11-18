# Desafio 71: Simulador de Caixa Eletrônico
# Objetivo:
# Simular um caixa eletrônico que pergunta o valor a ser sacado (número inteiro).
# O programa deve informar quantas cédulas de cada valor serão entregues.
# Cédulas disponíveis: R$50,0 R$20,0 R$10,0 R$1,0

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Valor para saque: R$ '))
total = valor
cedula = 100
total_cedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R${cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        total_cedulas = 0
        if total == 0:
            break
print('-' * 30)
print('Volte senpre ao Banco CEV!')