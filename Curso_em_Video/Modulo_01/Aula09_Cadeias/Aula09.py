frase = 'Curso em Video Python'
print(frase)
print()
#fatiamento
print('Fatiamento')
print(frase[9:14]) #Do caracter 9 ao 14.
print(frase[9:14:2]) #Do caracter 9 ao 14, pulando de 2 em 2.
print(frase[:14]) #Do caracter inicial ao 14.
print(frase[15:]) #Do caracter 15 ao final.
print(frase[9::3]) #Do caracter 9 ao final, pulando de 3 em 3.
print()
#Analise de Str
print('Analise')
print(len(frase)) #Irá analisar a 'frase' e indicar quantos caracters existem (contando com os espaços).
print(frase.count('o')) #Irá contar quantas vezes o str 'o' aparece.
print(frase.count('o', 0, 13)) #Anlise + Fatiamento.
print(frase.find('deo')) #(find = encontrar) ira indicar onde a caracter se inicia.
print(frase.find('Android')) #Indica (-1) quando a str não existe.
print('curso' in frase) #Irá responder se 'curso' existe em 'frase'.
print()
#Transformação
print('Transformação')
print(frase.replace('Python', 'Android')) #(replace = trocar/reposicionar) Irá substituir a str.
print(frase.upper()) #Irá mudar as caracteres minusculas para maiusculas.
print(frase.lower()) #Irá mudar as caracteres em maiusculo para minusculas.
print(frase.capitalize()) #Irá mudar todas as caracters para minusculos exceto a primeira.
print(frase.title()) #Irá analisar quantas palavras existem na str, e fazer o 'capitalize' palavra por palavra.
nova_frase = str(input('Frase: '))
print(nova_frase.strip()) #Irá eliminar os espaços desnecessarios, assim como 'rstrip' e 'lstrip'.
print()
#Divisão
print('Divisão')
print(frase.split()) #Irá dividir a str, a partir dos espaços, gerando uma lista com todas as palavras.
print('Junção')
print('_'.join(frase)) #Irá juntar a str, trocando os espaços, pela caracter indicada '-'.