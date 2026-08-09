# Este é o arquivo número 92
#O que fazer: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e registe-os (com idade) num dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa se vai aposentar.
from datetime import date
ano_atual = date.today().year

ctps = {}

nome = str(input('Nome completo: '))
sexo = str(input('Sexo [M/F]: ')).upper()
ano_nasc = int(input('Ano de Nascimento: '))
idade = ano_atual - ano_nasc
codigo_ctps = int(input('Código CTPS (Se não tiver digite 0): '))

ctps.update({'Nome': nome, 'Sexo': sexo, 'Data de nascimento': ano_nasc, 'Idade': idade, 'CTPS': codigo_ctps})

if codigo_ctps != 0:
    ano_contrato = int(input('Ano de Contratação: '))
    salario = float(input('Salario: R$'))
    
    ctps.update({'Ano de contratação': ano_contrato, 'Salario': salario})
else:
    mensagem = ('Sem CTPS cadastrado')
    ctps.update({'CTPS': mensagem})

print('==+=='* 10)
for c, v in ctps.items():
    print(f'{c}: {v}')
    

