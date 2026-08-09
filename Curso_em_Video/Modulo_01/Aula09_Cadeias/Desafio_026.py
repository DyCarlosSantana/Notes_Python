frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes no seu nome.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')-1)) #rfind: inicia a procura do lado direito.