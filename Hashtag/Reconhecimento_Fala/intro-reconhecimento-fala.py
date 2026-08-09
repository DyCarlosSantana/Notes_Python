# instalação: SpeechRecognition e PyAudio
# para pyaudio, digite no googles "install pyaudio (sistema operacional)" no windows seria se não funcionar o "pip install pyaudio" ou "pipwin install pyaudio"

import speech_recognition as sr #Recomendação da documentação (apelido para o pacote "speech_recognition    ")

rec = sr.Recognizer()

# Para ver os microfones do seu computador
# print(sr.Microphone.list_microphone_names())
# O microfone padrão do computador é o 0 e não é necessário coloca-lo na variável mic, caso seja usado outro o valor do micrifone na lista dever ser colocado na variável mic

print("Iniciando o Reconhecimento de Fala")
with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    # Acima chamamos o Recognizer e ele ajusta o microfone para que ele não entenda ruídos. Passamos a variável mic para que ele entenda o microfone que será usado.

    print("Pode Falar...") # Para indicar ao usuario que ele pode falar
    audio = rec.listen(mic) 
    # Aqui ele ouve o que o usuario fala e armazena na variável audio

    texto = rec.recognize_google(audio, language="pt-BR") 
    # Aqui ele reconhece o que o usuario falou usando a ferramenta do google e armazena na variável texto, repassando como parametro o variavel com o audio e o idioma
    print(texto)