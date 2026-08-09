#Verificando se o nome da cidade tem 'Santo'...

cidade = str(input('Digite o nome da sua cidade: ')).strip()
verificacao = cidade[:5].upper() == 'SANTO' or cidade[:5].upper() == 'SANTA'
print(verificacao)