import speech_recognition as sr

#Habilita o microfone para ouvir o usuario
microfone = sr.Recognizer()
with sr.Microphone() as source:
    #Chama a funcao de reducao de ruido disponivel na speech_recognition
    microfone.adjust_for_ambient_noise(source, duration=1)

    try:
        #Avisa ao usuario que esta pronto para ouvir
        print("Diga alguma coisa: ")
        #Armazena a informacao de audio na variavel
        audio = microfone.listen(source, timeout=2, phrase_time_limit=4)
    except sr.WaitTimeoutError:
        print("Tempo para falar passou do limite")
        exit()
    
try:
    #Passa o audio para o reconhecedor de padroes do speech_recognition
    frase = microfone.recognize_google(audio,language='pt-BR')
    print(frase)

    #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
except sr.UnknownValueError:
    print("Não entendi")
