salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo_salario = salario + (salario *15 / 100)
else:
    novo_salario = salario + (salario *10 / 100)
print('Seu salário era de R${:.2f} e agora com o aumento passou a ser R${:.2f}'.format(salario, novo_salario))