import os
from dotenv import load_dotenv
from rich.traceback import install
from rich.console import Console
from rich.panel import Panel
from groq import Groq
# biblioteca usada para recohecimento de fala + PyAudio (python -m pip install pyaudio)
import speech_recognition as sr 

install()
load_dotenv() # Carrega as variáveis do ficheiro .env

console = Console()
chave_api = os.getenv("GROQ_API_KEY")

# Função feita apenas para facilitar o uso da função Panel da biblioteca Rich
def painel(msg, titulo = "Mensagem", cor_borda = "blue", tamanho = 80):
    painel_msg = Panel(msg, title=titulo, border_style=cor_borda, width=tamanho)
    console.print(painel_msg)

# Verifica se o .env esta configurado corretamente
if not chave_api:
    painel("\n[bold red]❌ ERRO: Chave da API do Groq não encontrada![/bold red]", titulo="AVISO", cor_borda='red')
    exit()

cliente = Groq(api_key=chave_api)
## Já inicializamos com a "personalidade"
historico_mensagens = [{"role": "system", "content": "Seu nome é Cleitinho, um mentor programação Python muito didático"}]


# Intanciando o Recognizer - Conjunto de configurações
rec = sr.Recognizer()
# O padrão é 0.8 segundos. Para almentar usamos ".pause_threshold" que recebe 1.5
rec.pause_threshold = 1.5

while True:
    try:
        painel("Digite [yellow]'voz'[/] para falar \nDigite [yellow]'sair'[/] para encerrar", cor_borda="yellow")
        pergunta = input("\nComo posso ajudar?: ").strip()
        if pergunta.lower() == "sair":
            break
        elif pergunta.lower() =="voz":
            with sr.Microphone() as mic:
                #Calibra o reconhecedor ao ruído de fundo do seu ambiente para melhorar a precis
                rec.adjust_for_ambient_noise(mic)
                painel("Pode falar...", titulo="| 🎙️   |", tamanho=40)
                try:
                    # .listen captura a entrada de áudio de um microfone ou de um arquivo de áudio e a converte em uma AudioData instância (precisa ser instanciada).
                    # Adicionado timeout: Se houver 5 segundos de silêncio, ele desiste em vez de travar o programa
                    audio = rec.listen(mic, timeout=5) 
                    
                    # Converte a captura de áudio para texto
                    texto_audio = rec.recognize_google(audio, language="pt-BR")
                    painel(texto_audio, titulo="Você disse:")
                    pergunta = texto_audio
                    
                except sr.UnknownValueError:
                    painel("Desculpe, não consegui entender o áudio. Tente novamente.", titulo="Erro de Voz", cor_borda="red")
                    continue # Pula esse turno e volta ao início do 'while'
                except sr.WaitTimeoutError:
                    painel("Nenhuma voz detectada. O microfone foi desligado por inatividade.", titulo="Silêncio", cor_borda="yellow")
                    continue

        # Adiciona a pergunta atual ao histórico ANTES de chamar a API
        historico_mensagens.append({"role": "user", "content": pergunta})
        resposta = cliente.chat.completions.create(
            messages=historico_mensagens,
            model="llama-3.1-8b-instant"
        )

        resposta_da_ia = resposta.choices[0].message.content
        # Guarda a resposta da IA no histórico com a role 'assistant' para o próximo turno
        historico_mensagens.append({"role": "assistant", "content": resposta_da_ia})

        painel(resposta_da_ia, titulo="Resposta - Cleitin", cor_borda="green")

    except Exception as e:
        aviso = (f"\n[bold red]❌ ERRO DESCONHECIDO NA API:[/bold red]\n{str(e)}")
        painel_aviso_falha = Panel(aviso, title="AVISO", border_style="red", width=80)
        console.print(painel_aviso_falha)