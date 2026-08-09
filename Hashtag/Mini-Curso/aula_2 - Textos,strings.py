faturamento = 1000
custo = 600
lucro = faturamento - custo
texto = f"O lucro foi de {lucro} e o faturamento foi de {faturamento}" 
#concatenar -> usado para unir duas ou mais cadeias de texto em uma única cadeia

print(texto)

#Quebra de Textos
email = "email_falso@gmail.com"
email = email.lower() #transforma tudo em minusculos
email = email.upper() #transforma tudo em maisculos
email = email.strip() #Retira espaços (antes e depois) da str
print(email)

#Tamanho
print(len(email)) #analisa a str e informa quantas caracteres existem a partir da caracter 0.

#Posição
posição = email.find('@') #procuea a caracter e informa a posição dela (a variavel recebe a posição da caracter)
print(posição)

#pedaços do texto

print(email[11])
print(email[11:17]) 
#print(email[11:]) 
#usando a função (find) em conjunto con o fatiamento de texto para encontrar e imprimir a parte desejada
servidor = print(email[posição:]) 
servidor = print(email[posição+1:]) 
servidor = print(email[:posição]) 

#trocar uma parte do texto
novo_email = email.replace('gmail.com', 'hotmail.com')
print(novo_email)

nome = 'Edy Carlos'
nome = nome.capitalize() #primeira caracter em maiuscula
print(nome)
nome = nome.title() #primeira caracter apos cada espaço em maiusculas
print(nome)
nome = nome.upper() #todas em maiusculas
print(nome)

#formatação numerica
faturamento = 1000
custo = 600
lucro = faturamento - custo
margem = lucro / faturamento
texto = f"O lucro foi de {lucro:,.2f} e o faturamento foi de {faturamento:,.2f}, e a margem foi de {margem:.1%}"  #Separador de milhar {lucro:,}. Casas decimais {lucro:.2f}
print(texto)

#EXERCÍCIO  
#Descubra o servidor do Email 
#Descubra o primeiro nome do usuario
#Crie uma mensagem personalizada com o "primeiro nome"
print('')
print('---'*15)

nome = str(input('NOME: ')).upper()
email = str(input('INFORME SEU E-MAIL: ')).upper()
#resolução
posição = email.find('@') #Descobrir a posição
servidor = (email[posição+1:]) #atraves da posição descobrir o servidor
p_nome = nome.split() #descobrir o primeiro nome separando a frase em uma lista (uma das formas)
mensagem = (f'Usuario {p_nome[0, 1]} foi cadastrado com sucesso!')
print('---'*15)
print(nome)
print(email)
print(mensagem)
