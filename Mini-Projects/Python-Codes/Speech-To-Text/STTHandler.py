import speech_recognition as sr
import os
import sys

class STTHandler:
    def __init__(self) -> None:
        self.microphone = sr.Recognizer()
        self.source = sr.Microphone()

    def clear_console(self):
        if (sys.platform == 'win32'):
            os.system('CLS')
        else: 
            os.system('clear')

    def get_phrase_from_voice(self) -> str:
        with self.source as source:
            #Chama a funcao de reducao de ruido disponivel na speech_recognition
            self.microphone.adjust_for_ambient_noise(source)
            self.clear_console()        

            try:
                #Avisa ao usuario que esta pronto para ouvir
                print("Say something: ")
                #Armazena a informacao de audio na variavel
                audio = self.microphone.listen(source, timeout=2, phrase_time_limit=4)
            except sr.WaitTimeoutError:
                print("Time to speak exceed")
                return ''
            
        try:
            #Passa o audio para o reconhecedor de padroes do speech_recognition
            phrase = self.microphone.recognize_google(audio,language='pt-BR')
            return phrase

        #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
        except sr.UnknownValueError:
            print("Don't understand")
            return ''
