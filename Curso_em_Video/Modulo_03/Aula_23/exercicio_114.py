# Resolução mais atual
import urllib.request
import urllib.error
# Configuração do URL do alvo
url = 'http://www.pudim.com.br'

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'} #Criando um User Agent

# Criando a requisição
requisicao = urllib.request.Request(url, headers=headers)
try:
    site = urllib.request.urlopen(requisicao)
except urllib.error.URLError as erro:
    print('\033[31mO site Pudim não está acessível no momento.\033[m')
    print(f'Motivo do erro: {erro.reason}') # razão pelo qual o site não consegue ser acessado
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
    
# Resolução basica
"""
import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError as erro:
    print('O site Pudim não está acessível de momento.')
    print(f'Erro identificado: ({erro})')
else:
    print('Consegui aceder ao site Pudim com sucesso!')
"""

# Abre a URL e lê o conteúdo da página
"""
with urlopen('https://www.python.org') as response:
    html = response.read()
    print(html.decode('utf-8')) # Decodifica o conteúdo para texto
"""
