import os
import json
from dotenv import load_dotenv
from rich.traceback import install
from rich.console import Console
from rich.panel import Panel
from groq import Groq

install()
load_dotenv() # Carrega as variáveis do ficheiro .env

console = Console()
chave_api = os.getenv("GROQ_API_KEY")

# Verifica se o .env esta configurado corretamente
if not chave_api:
    aviso = ("\n[bold red]--- ERRO: Chave da API do Groq não encontrada! ---[/bold red]")
    painel_aviso_falha = Panel(aviso, title="AVISO", border_style="red", width=80)
    console.print(painel_aviso_falha)
    exit()

cliente = Groq(api_key=chave_api)

# Indica o caminho para o arquivo que vai ser lido
path = "Desenvolvimento_Cleitinho/Exercicio_04/doc_texto_bagunçado.txt"
if not os.path.exists(path): # Verifica se o caminho existe
    aviso = (f"\n[bold red]--- ERRO: O ficheiro '{path}' não foi encontrado! ---[/bold red]")
    console.print(Panel(aviso, title="AVISO", border_style="red"))
    exit()
else:
    aviso = (f"[green]--- Ficheiro '{path}' carregado com sucesso ---[/]")
    console.print(Panel(aviso, title="Anexo", border_style="green"))
    with open(path, 'r', encoding="utf-8") as f:
        conteudo_ficheiro = f.read()

try:
    # Adiciona a pergunta atual ao histórico ANTES de chamar a API
    resposta = cliente.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"Você ajuda no processo de arquivos e dados. Analise o ficheito anexado, e retorne uma estrutura formato em JSON, com as chaves: nome - referente ao nome do cliente, produto - uma lista com nome_produto, quantidade, valor e subtotal, e valor_total - referente a somatoria total de compra. Seguindo a estrutura JSON exigida, sendo sempre direto e objetivo"},
            {
                "role": "user",
                "content": conteudo_ficheiro
            }
            ],
        model="llama-3.1-8b-instant",
        response_format={"type": "json_object"}
    )

    resposta_chat = resposta.choices[0].message.content
    estrutura_organizada = json.loads(resposta_chat)
    
    painel_resposta = Panel(str(estrutura_organizada), title="Dicionario Python Gerado:", subtitle="Digite 'sair' para encerrar a sessão", border_style="green", width=80)
    console.print(painel_resposta)

except Exception as e:
    aviso = (f"\n[bold red]❌ ERRO DESCONHECIDO NA API:[/bold red]\n{str(e)}")
    painel_aviso_falha = Panel(aviso, title="AVISO", border_style="red", width=80)
    console.print(painel_aviso_falha)
