#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador, e em quantos anos ele vai pagar.
#Calcular o valor da prestação mensal, sabendo que ele não pode exceder 30% do salario ou então o emprestimo será negado

#Coleta dos dados:
nome = str(input('Digite seu nome: ')).strip()
renda_mensal = float(input('Informe sua renda mensal: '))
valor_imovel = float(input('Informe o valor do imovel: '))
anos = int(input('Em quantos anos pretende pagar o emprestimo?: '))
print('PROCESSANDO...')

#Calculo
prestacao = valor_imovel / (anos * 12)
limite = renda_mensal * 30 /100

#Verificação
if prestacao > limite:
    print('Emprestimo NEGADO!')
else:
    print('{}, seu emprestimo foi APROVADO!'.format(nome))
    print('O valor da prestação mensal será de R${:.2f}'.format(prestacao))