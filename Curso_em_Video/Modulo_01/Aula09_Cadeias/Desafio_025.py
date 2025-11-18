#Verificando se tem "Silva" no nome...

nome_completo = str(input('Digite seu nome completo: ')).strip().upper()
print('Seu nome tem Silva? {}'.format('SILVA' in nome_completo))