#Analise de nome...

nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em maiusculo é: ', nome.upper()) #Maiusculas
print('Seu nome em minuscuo é: ', nome.lower()) #Minusculas
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #Contagem de caracters (sem espaço)
dividido = nome.split() # Dividindo o nome em uma lista.
print('Seu primeiro nome é: {}, e tem {} letras.'.format(dividido[0], len(dividido[0]))) #selecionando o primeiro item da lista e imprimindo.
