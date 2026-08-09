import os
from dotenv import load_dotenv
from groq import Groq
from rich.traceback import install
from rich.console import Console
from rich.panel import Panel
install()

# Carrega as variáveis do ficheiro .env
load_dotenv() 

console = Console()

# Busca a chave específica do Groq no ficheiro .env
chave_api = os.getenv("GROQ_API_KEY")

# Verifica se o .env esta configurado corretamente
if not chave_api:
    aviso = ("\n[bold red]❌ ERRO: Chave da API do Groq não encontrada![/bold red]")
    painel_aviso_falha = Panel(aviso, title="Conectando", border_style="blue", width=60)
    console.print(painel_aviso_falha)
    exit()

# Instancia um objeto da classe Gloq que serve como ligação direta com servidores na nuvem.
cliente = Groq(api_key=chave_api) 

pergunta = input("Digite algo: ")

try:
    aviso = ("[blue]Carregando Resposta...[/]")
    painel_aviso = Panel(aviso, title="Conectando", border_style="blue", width=60)
    console.print(painel_aviso)

    # O Groq usa uma estrutura padrão de mercado (similar à da OpenAI)
    resposta = cliente.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": pergunta,
            }
        ],
        model="llama-3.1-8b-instant", # Modelo usado
    )
    
    conteudo = resposta.choices[0].message.content
    painel_resposta = Panel(conteudo, title="Resposta (Groq):", border_style="green", width=60)
    console.print(painel_resposta)

except Exception as e:
    console.print(f"\n[bold red]❌ ERRO DESCONHECIDO NA API:[/bold red]\n{str(e)}")